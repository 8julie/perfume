import time # being nice <3
import requests
import re
from bs4 import BeautifulSoup

from urllib.parse import urlparse, urljoin

import json

import os

class Scraper():
    def __init__(self, url):
        """Instantiates scraping from URL"""
        self.url = url
        self.parsed_url = urlparse(self.url)
        self.fn_index = ""
    
    def makeIndex(self, *args):
        soup = self.scrape(args)
        fn = self.saveIndex(soup)
        return fn

    def save(file_name, info):
        """Writes data into a json file"""
        file_name += '.json'
        with open(file_name, 'w', encoding='latin-1') as f:
            json.dump(info, f, indent=8, ensure_ascii=False)
        
        return file_name

    def scrape(self, *args):
        if (args == True):
            scrape_url = args[0] # lol
        else:
            scrape_url = self.url


        """A simple scraper"""
        response = requests.get(scrape_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        time.sleep(4) # optional ..... i'm just being nice
        return soup

    def saveIndex(self, soup, fn="index"):
        """Assumes self.url contains index, gets items/frag bases"""

        res = []

        # Selects the link
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
        # fn = "index"
        return Scraper.save(fn, res)

    def loadIndex():
        with open('index.json', 'r') as file:
            data = json.load(file)
        
        return data

    def scrapeIndex(self):
        """Scrapes based on index.json"""

        # Loads the data
        if (os.path.exists("index.json")):
            data = self.loadIndex()
        else:
            self.scrape()

        
        for item in data:
            soup = Scraper.scrape(item['link'])
            items = soup.find("td", class_="wrd80")

            print(items.get_text())

        time.sleep(4) # optional ..... i'm just being nice
        
        pass

    def saveProfile(self, soup):
        """Helper for scrapeIndex"""
        pass
    

if __name__ == "__main__":
    url = 'https://www.thegoodscentscompany.com/peb-az.html' # very rudimentary but it's just 1 link! who cares
    Scraper(url)
    Scraper.scrapeIndex()
