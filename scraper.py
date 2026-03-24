import time # being nice <3
import requests
import re
from bs4 import BeautifulSoup

import json

from urllib.parse import urlparse, urljoin

def scrape(site_url):
    """A simple scraper"""

    res, base_no = [], 1
    base_url = urljoin(urlparse(site_url).scheme, urlparse(site_url).netloc)

    response = requests.get(url)
    time.sleep(4) # optional ..... i'm just being nice
    soup = BeautifulSoup(response.text, 'html.parser')

    # Selects
    pattern = r'data.*html'
    on_clicks = soup.find_all('a', {'onclick' : re.compile(pattern)})

    # Parses and puts it somewhere
    for item in on_clicks:
        name = item.get_text().replace("specialty", "")
        link = re.findall(pattern, item['onclick'])[0]
        absolute_link = base_url + "/" + link

        data = {'name': name, 'link': absolute_link}

        res.append(data)
        base_no += 1

    return res

def save(file_name, info):
    """Writes data into a json file"""
    file_name += '.json'
    with open(file_name, 'w', encoding='latin-1') as f:
        json.dump(info, f, indent=8, ensure_ascii=False)

if __name__ == '__main__':
    url = 'https://www.thegoodscentscompany.com/peb-az.html' # very rudimentary but it's just 1 link! who cares
    res = scrape(url)
    save("peb", res)