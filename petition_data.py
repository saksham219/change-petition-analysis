from bs4 import BeautifulSoup
import requests
import json
import re


data = requests.get('https://www.change.org/api-proxy/-/petitions/8091143/updates/recent').json()

print(data)
n_updates = len(data)

petition = data[0]['petition']

id = petition['id']
ask = petition['ask']
title = petition['title']
city = petition['relevant_location']['city']
country_code = petition['relevant_location']['country_code']
lat = petition['relevant_location']['lat']
lng = petition['relevant_location']['lng']
description = petition['description']
created_at = petition['created_at']
locality = petition['original_locale']

for d in petition['targets']:
    print(d['display_name'])
    print(d['description'])
    print(d['additional_data']['title'])
    print(d['locale'])

creator = petition['creator_name']
signs = petition['displayed_signature_count']
status = petition['petition_status']
victory = petition['is_victory']

print(id, ask, title, city, country_code, lat, lng, description,'\n', created_at, locality, creator, signs, status, victory)
