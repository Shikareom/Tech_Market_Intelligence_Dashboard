import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def scrape_naukri():
    # Start the browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = "https://www.naukri.com/data-science-jobs-in-pune"
    driver.get(url)
    
    
    time.sleep(10) 
    
    #Extracting page source
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    job_cards = soup.find_all('div', class_='srp-jobtuple-wrapper')
    
    data = []
    for card in job_cards:
        try:
            # We use .get_text() and strip() to clean the data immediately
            title = card.find('a', class_='title').get_text(strip=True)
            company = card.find('a', class_='comp-name').get_text(strip=True)
            exp = card.find('span', class_='exp-wrap').get_text(strip=True)
            
            # Skills are tricky—they are a list of items
            skill_list = [s.get_text(strip=True) for s in card.find_all('li', class_='dot-gt')]
            skills_string = ", ".join(skill_list)
            
            data.append({
                "Job_Title": title,
                "Company": company,
                "Experience": exp,
                "Skills": skills_string
            })
        except AttributeError:
            continue # Skip ads
            
    driver.quit()
    return pd.DataFrame(data)

# Run and Save
df_jobs = scrape_naukri()
df_jobs.to_csv("pune_jobs_raw.csv", index=False)
print("Step 1 Complete: Raw data saved to CSV!")