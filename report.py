#!/usr/bin/env python3

import math
import requests

USER = 'junaruga'
SEARCH_URL_FORMAT = 'https://api.github.com/search/issues?q=user:{user}&page={page}'
# Default items per page is 30.
# https://developer.github.com/v3/#pagination
PER_PAGE = 30

url = SEARCH_URL_FORMAT.format(user=USER, page=1)
response = requests.get(url)
json = response.json()
total_count = json['total_count']
total_page_num = math.floor(total_count / PER_PAGE) + 1

item_count = 0
for count in range(total_page_num):
    page = count + 1

    url = SEARCH_URL_FORMAT.format(user=USER, page=page)
    # print('URL: {0}'.format(url))
    response = requests.get(url)
    json = response.json()

    items = json['items']
    for item in items:
        title = item['title']
        html_url = item['html_url']
        print('- {0}\n  {1}'.format(title, html_url))

        item_count += 1

print('item_count: {0}'.format(item_count))
