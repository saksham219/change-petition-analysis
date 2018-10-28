from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium import webdriver


chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome("C:/Users/user/desktop/chromedriver",chrome_options=chrome_options)
driver.get(url ='https://www.change.org/p/free-nazanin-ratcliffe?source_location=discover_feed')

sleep(2)


data = driver.page_source

soup = BeautifulSoup(data, 'lxml')

title = soup.find('h1', {'class':'mtl mbxxxl xs-mts xs-mbxs petition-title'}).text

print(title)

a =soup.find('strong',{'class' : 'type-s type-weak'})

b = a.find_all('a')

starter_name = b[0].text

to_name = b[1].text

print(starter_name)
#print(to_name)

desc = soup.find('div',{'class': 'rte js-description-content'}).text
#print(desc)

wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='4 others']"))).click()
sleep(2)

data=driver.page_source

soup = BeautifulSoup(data, 'html.parser')
html = soup.prettify("utf-8")
with open("C:\\Users\\user\\desktop\\output1.html", "wb") as file:
    file.write(html)

#letters1=soup.find_all("strong",attrs={'class': 'link-subtle'})
#print(letters1) 
#positions1 = soup.find_all("div",attrs={'class': 'type-weak type-ellipsis'})
#print(positions1)



a = soup.find_all("div",attrs={'class': 'type-ellipsis'})
print(a)

for p in a:
    name =     p.find('strong', attrs = {'class': ['link-subtle', '']})
    if name:
        print(name.text)
    position = p.find('div', attrs = {'class': 'type-weak type-ellipsis'})
    if position:
        print(position.text)
        
#prints names of 4 others
print( "\n")
for i in letters1:
    print (i.text)
