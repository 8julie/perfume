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

    def scrape(self, url="", parser="html.parser") -> BeautifulSoup:
        """A simple scraper"""

        if (url == ""):
            url = self.url  


        response = requests.get(url)
        soup = BeautifulSoup(response.text, parser)
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

        if (os.path.exists("index.json")):
            data = Scraper.loadIndex()
        else:
            self.makeIndex()

        res = []

        for item in data:
            link = item['link']
            name = item['name']

            print(name, link)
            soup = self.scrape(link).find_all("td", class_="wrd80")

            for res in soup:
                ingr_link = res.find('a').get('href')
                ingr_name = re.sub(r'(FR)|(FL)|(\/)', "", string=res.get_text())

                data = {
                    'name':name,
                    'ingr_name': ingr_name,
                    'ingr_link': ingr_link
                }
                res.append(data)
            Scraper.save(name, res)
            res = []

            time.sleep(4) # optional ..... i'm just being nice
        
        pass    

if __name__ == "__main__":
    url = 'https://www.thegoodscentscompany.com/peb-az.html' # very rudimentary but it's just 1 link! who cares
    Scraper(url)
    Scraper.scrapeIndex()
