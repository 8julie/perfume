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

        soup = Scraper.scrape(self.url)
        self.saveIndex(soup)


    def scrape(scrape_url):
        """A simple scraper"""
        response = requests.get(scrape_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        time.sleep(4) # optional ..... i'm just being nice
        return soup


    def saveIndex(self, soup):
        """Assumes self.url contains index, gets items/frag bases"""

        res = []

        # Selects
        link_pattern = r'data.*html'
        on_clicks = soup.find_all('a', {'onclick' : re.compile(link_pattern)})

        # Parses
        for item in on_clicks:
            name = item.get_text().replace("specialty", "")
            link = re.findall(link_pattern, item['onclick'])[0]
            absolute_link = "http://" + urljoin(self.parsed_url.scheme, self.parsed_url.netloc) + "/" + link # whatever man

            data = {'name': name, 'link': absolute_link}

            res.append(data)

        # Puts it somewhere
        
        fn = "index"
        save(fn, res)

    def scrapeIndex():
        """Scrapes based on index.json"""
        with open('index.json', 'r') as file:
            data = json.load(file)
            for item in data:
                soup = Scraper.scrape(item['link'])
                print(soup)
                break

if __name__ == "__main__":
    url = 'https://www.thegoodscentscompany.com/peb-az.html' # very rudimentary but it's just 1 link! who cares
    Scraper(url)
    Scraper.scrapeIndex()
