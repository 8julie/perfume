import time # being nice <3
import requests
import re
from bs4 import BeautifulSoup

from urllib.parse import urlparse, urljoin

import json

import os

import nltk

class Scraper():
    def __init__(self, url):
        """Instantiates scraping from URL"""
        self.url = url
        self.parsed_url = urlparse(self.url)
        self.fn_index = ""

    def testResponse(url:str)-> bool:
        """Tests response"""

        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if (response.status_code == 200):
            # Parse the HTML content using BeautifulSoup
            print(f"[SUCCESS] Page fetched successfully!  URL: ", url)
            return True
        else:
            print(f"[ERROR] Failed to retrieve page.  \n  URL: ", url, "\n Status code: {response.status_code} \n ---------------------->\n")
            return False

    def getAbsLink(self, ending) -> str:
        """Gets the absolute link"""

        absolute_link = "http://" + urljoin(self.parsed_url.scheme, self.parsed_url.netloc) + "/" + ending # whatever man
        return absolute_link

    def scrape(self, url="", parser="html.parser") -> BeautifulSoup | None:
        """A simple scraper"""

        if (url == ""):
            url = self.url  
        
        if (Scraper.testResponse(url)):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, parser)
            time.sleep(4) # optional ..... i'm just being nice

            return soup

        return None
    

    def tokenize(self):
        soup = self.scrape()
        string = soup.get_text()
    
        match = re.findall(r'.*[a-z] specialty', string, flags=re.IGNORECASE)

        if (match):
            print("[LOG] Match detected: ")
            print(match)

        else:
            print("[LOG] No match!")
            print("[LOG] Printing page: ")
            print(string)

        # print(pos)
        # tagged = nltk.pos_tag(tokens)
        # print(tagged)


    def getCAS(soup:BeautifulSoup):
        CAS_pattern = 2

        return 

    def save(file_name, info, folder_name=""):
        """Saves a file, with an optional folder for the name"""

        if (folder_name != ""):
            if (os.path.exists(folder_name) == False):
                os.mkdir(folder_name)
            file_name = folder_name + "/" + file_name

        """Writes data into a json file"""
        file_name += '.json'
        with open(file_name, 'w', encoding='latin-1') as f:
            json.dump(info, f, indent=8, ensure_ascii=False)
        
        return file_name

    def loadjson(fn='index.json'):
        with open(fn, 'r') as file:
            data = json.load(file)
        
        return data

if __name__ == "__main__":
    url = "https://www.thegoodscentscompany.com/peb-az.html"
    s = Scraper(url)
    s.tokenize()
    # soup = s.scrape()
    # tagged = Scraper.tokenize(soup)
    # adj = s.adjTokens(tokens)