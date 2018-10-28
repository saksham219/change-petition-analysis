from bs4 import BeautifulSoup
import requests
import json
import re

r = requests.get(url ='https://www.change.org/p/theresa-may-mp-stop-mp-s-drinking-alcohol-in-the-houses-of-parliament?source_location=discover_feed')

data = r.text

soup = BeautifulSoup(data, 'lxml')

title = soup.find('h1', {'class':'mtl mbxxxl xs-mts xs-mbxs petition-title'}).text

print(title)

a =soup.find('strong',{'class' : 'type-s type-weak'})

b = a.find_all('a')

starter_name = b[0].text

to_name = b[1].text

print(starter_name)
print(to_name)

desc = soup.find('div',{'class': 'rte js-description-content'}).text
print(desc)

b = soup.find('div', {'class': 'arrange-fill petition-byline-content'})
#print(b)


k = b.find('div')

text = str(k)

finds = [m.start() for m in re.finditer('\'', text)]

l = text[finds[0]+1: finds[1]]

k = json.loads(l)

for dm in k:
    print('name :', dm['display_name'])
    print('desc: ',dm['description'])
    print('locale: ', dm['locale'])
    print('title: ',dm['additional_data']['title'])

#print(k.text)
