import csv
import requests
from petition import Petition
from description import Description
from target import Target
import os
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium import webdriver
from constants import webdriver_path, descriptions_folder_path, petitions_csv_path, targets_csv_path
from constants import main_url


def get_url_from_type(page_type):
    if page_type == 'victories':
        return main_url  + page_type + '#featured/'
    else:
        return main_url + 'petitions' + '#' + page_type + '/'


def write_all(data, petition_id):
    petition = get_petition_data(data)
    description = get_desc_data(data)
    targets = get_targets(data)

    write_to_csv(petitions_csv_path, petition)                          # writing single petition to petitions csv

    write_to_text(get_textfile_path(petition_id), description)           # writing description to text file

    for target in targets:                                              # writing all targets to target csv
        write_to_csv(targets_csv_path, target)


def get_page_data(url, page_type):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(webdriver_path, chrome_options=chrome_options)
    driver.get(url=url)

    sleep(5)

    data=driver.page_source
    soup = BeautifulSoup(data, 'html.parser')
    petitions = soup.find_all('li', attrs={'class':'petition'})

    if page_type == 'victories':
        for petition in petitions[-10:]:
            petition_url = petition['data-url']
            petition_id = get_id_from_link(petition_url)
            petition_url = get_petition_url(petition_id)
            data = get_data(petition_url)
            print('collecting petition '+ petition_id + '...')
            write_all(data, petition_id)
    else:
        for petition in petitions:
            petition_id = petition['data-id']
            petition_url = get_petition_url(petition_id)
            data = get_data(petition_url)
            print('collecting petition '+ petition_id + '...')
            write_all(data, petition_id)


def get_petition_url(petition_id):
    return 'https://www.change.org/api-proxy/-/petitions/' + petition_id + '/updates/recent'


def get_textfile_path(petition_id):
    return descriptions_folder_path + petition_id + '.txt'

def write_to_csv(filename, obj):
    obj = vars(obj)
    fwrite = open(filename, 'a+')
    writer = csv.writer(fwrite, delimiter=',', lineterminator='\n')
    if os.fstat(fwrite.fileno()).st_size == 0:
        writer.writerow(obj.keys())
    writer.writerow(obj.values())
    fwrite.close()


def write_to_text(filename, obj):
    obj = vars(obj)
    text = obj['description']
    with open(filename, 'w') as f:
        f.write(text)


def get_data(url):
    data = requests.get(url).json()
    return data


def get_petition_data(data):
    updates = len(data)
    petition = data[0]['petition']
    petition_id = petition['id']
    ask = petition['ask']
    title = petition['title']
    city = petition['relevant_location']['city']
    country_code = petition['relevant_location']['country_code']
    lat = petition['relevant_location']['lat']
    lng = petition['relevant_location']['lng']
    created_at = petition['created_at']
    locality = petition['original_locale']
    creator = petition['creator_name']
    signatures = petition['displayed_signature_count']
    status = petition['petition_status']
    victory = petition['is_victory']
    victory_date = petition['victory_date']

    petition_obj = Petition(petition_id, ask, title, city, country_code,lat, lng, created_at,
                            locality, creator, updates, signatures, status, victory, victory_date)

    return petition_obj


def get_desc_data(data):
    description_obj = Description(data[0]['petition']['description'])
    return description_obj


def get_targets(data):
    target_objs = []
    petition = data[0]['petition']
    for i,d in enumerate(petition['targets']):
        petition_id = petition['id']
        name = d['display_name']
        description = d['description']
        title = d['additional_data']['title']
        locale = d['locale']
        is_primary = True if i == 0 else False

        target_objs.append(Target(petition_id, name, description, title, locale, is_primary))

    return target_objs


def get_id_from_link(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    a = soup.find('div', attrs = {'class':'emergency_banner'})
    petition_id = a['data-petition_id']
    return petition_id
