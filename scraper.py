import time # being nice <3
import requests
import re
from bs4 import BeautifulSoup

from urllib.parse import urlparse, urljoin

import json

def save(file_name, info):
    """Writes data into a json file"""
    file_name += '.json'
    with open(file_name, 'w', encoding='latin-1') as f:
        json.dump(info, f, indent=8, ensure_ascii=False)


class Scraper():
    def __init__(self, url):
        self.url = url # intended to be the index
        self.parsed_url = urlparse(self.url)
        self.base_url = urljoin(self.parsed_url.scheme, self.parsed_url.netloc)

        self.scrape()
        self.saveIndex()


    def scrape(self):
        """A simple scraper"""
        response = requests.get(url)
        self.soup = BeautifulSoup(response.text, 'html.parser')
        time.sleep(4) # optional ..... i'm just being nice

    
    def saveIndex(self):
        """Assumes self.url contains index, gets items/frag bases"""

        res = []

        # Selects
        link_pattern = r'data.*html'
        on_clicks = self.soup.find_all('a', {'onclick' : re.compile(link_pattern)})

        # Parses
        for item in on_clicks:
            name = item.get_text().replace("specialty", "")
            link = re.findall(link_pattern, item['onclick'])[0]
            absolute_link = self.base_url + "/" + link

            data = {'name': name, 'link': absolute_link}

            res.append(data)

        # Puts it somewhere
        
        fn = "index"
        save(fn, res)

    

if __name__ == "__main__":
    url = 'https://www.thegoodscentscompany.com/peb-az.html' # very rudimentary but it's just 1 link! who cares
    Scraper(url)