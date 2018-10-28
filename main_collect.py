import requests
import json
import re
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium import webdriver

chrome_options = Options()
chrome_options.add_argument("--headless")

#url = 'https://www.change.org/en-GB/petitions?hash=recommended&hash_prefix=&list_type=default&view=recommended&page=2'
#url = 'https://www.change.org/petitions#featured'
#url = 'https://www.change.org/en-GB/petitions?view=this-week&page=1&hash=this-week&hash_prefix=this-week&first_request=true&list_type=default'
url = 'https://www.change.org/petitions#this-week/2'
driver = webdriver.Chrome("C:/Users/user/desktop/chromedriver",chrome_options=chrome_options)
driver.get(url =url)

sleep(10)

data=driver.page_source


soup = BeautifulSoup(data, 'html.parser')
html = soup.prettify("utf-8")


k = soup.find_all('li', attrs = {'class':'petition'})
print(len(k))

print(k[0]['data-id'], k[1]['data-id'])

wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='next button']"))).click()

sleep(10)
#link = driver.find_element_by_link_text('Next >>')
#link.click()

#link = driver.find_elements_by_class_name("next-button")
#print(link)
data = driver.page_source

#data = driver.page_source
soup2 = BeautifulSoup(data, 'html.parser')
html = soup2.prettify("utf-8")

print(html)

k = soup2.find_all('li', attrs = {'class':'petition'})
print(len(k))
print(k[10]['data-id'], k[11]['data-id'])
