#!/usr/bin/env python3

import requests

USER = 'junaruga'
SEARCH_URL_FORMAT = 'https://api.github.com/search/issues?q=user:{user}'

url = SEARCH_URL_FORMAT.format(user=USER)

response = requests.get(url)
items = response.json()['items']

for item in items:
  title = item['title']
  html_url = item['html_url']
  print('- {0}\n  {1}'.format(title, html_url))
