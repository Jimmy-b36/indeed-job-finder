import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def get_url(position, location, remote, age, language, radius):
  template = 'https://ca.indeed.com/jobs?q={}&l={}&sc=0kf%3A{}{}%3B&fromage={}&radius={}'
  position = position.replace(' ', '+')
  location = location.replace(' ', '+')
  remote = remote.replace(' ', '+')
  age = age.replace(' ', '+')
  language = language.replace(' ', '+')
  url = template.format(position, location, remote, language, age, radius)
  return url

def save_data_to_file(records):
  with open('results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['JobTitle', 'Company', 'Location', 'Post date', 'Date','Summary', 'JobURL'])
    writer.writerows(records)

def get_record(card):
    #Extract job data from single card
    job_title = card.find_element(By.CLASS_NAME,'jobTitle').text
    company = card.find_element(By.CLASS_NAME,'companyName').text
    location = card.find_element(By.CLASS_NAME,'companyLocation').text
    post_date = card.find_element(By.CLASS_NAME,'date').text
    extract_date = datetime.today().strftime('%Y-%m-%d')
    summary = card.find_element(By.CLASS_NAME,'job-snippet').text
    job_url = card.find_element(By.CLASS_NAME,'jcs-JobTitle').get_attribute('href')
    return (job_title, company, location, post_date, extract_date, summary, job_url)


def get_page_records(card, job_list, url_set):
    record = get_record(card)
    # add if job title exists and not duplicate
    if record[0] and record[-1] not in url_set:
        job_list.append(record)
        url_set.add(record[-1])



def main(keywords,position, location, remote, age, language, radius):
    scraped_jobs = []
    scraped_urls = set()
    
    url = get_url(position, location, remote, age, language, radius)
    
    # setup web driver
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://ca.indeed.com/")
    driver.implicitly_wait(5)
    driver.get(url)        
    
    # extract the job data
    while True:
        driver.implicitly_wait(5)
        # get all cards on page
        cards = driver.find_elements(By.CLASS_NAME,'slider_container')
        try:
          for element in cards:
            driver.implicitly_wait(10)
            element.click()
            driver.implicitly_wait(10)
            description = WebDriverWait(driver, 10).until(
              EC.presence_of_element_located((By.ID, "jobDescriptionText"))
            )
            #check to see if key word is in description
            for word in keywords:
              if word in description.text:
                break
              else: 
                get_page_records(element, scraped_jobs, scraped_urls) 
        except TimeoutException:
          continue    
        except ElementNotInteractableException:
          driver.find_element(By.ID,'popover-x').click()  # to handle job notification popup
          continue
        except ElementClickInterceptedException:
          continue
        finally:
          try:
            #continue on to next page
            driver.find_element(By.XPATH,'//a[@aria-label="Next Page"]').click()
          except NoSuchElementException:
              break
          except ElementNotInteractableException:
              driver.find_element(By.ID,'popover-x').click()  # to handle job notification popup
              continue
          
        
            
        
    
    # close driver and save records
    driver.quit()
    print('Total jobs scraped: ', len(scraped_jobs))
    save_data_to_file(scraped_jobs)

