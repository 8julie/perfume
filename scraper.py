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

    def makeIndex(self, url=""):
        """Creates `index.json`
        
        Returns file name of index
        """

        if (url == ""):
            url = self.url

        soup = self.scrape(url)
        fn = self.saveIndex(soup)
        return fn

    def scrape(self, url="", parser="html.parser") -> BeautifulSoup:
        """A simple scraper"""

        if (url == ""):
            url = self.url  


        response = requests.get(url)
        soup = BeautifulSoup(response.text, parser)
        time.sleep(4) # optional ..... i'm just being nice
        return soup

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

    def saveIndex(self, soup, fn="index"):
        """Creates `/ingredients`
        
        file name = index:idx
        idx = fragrance idx
        name = fragrance ingredient
        link = link to ingredient information"""

        res = []
        idx = 1

        # Selects the link
        link_pattern = r'data.*html'
        on_clicks = soup.find_all('a', {'onclick' : re.compile(link_pattern)})

        # Parses
        for item in on_clicks:
            name = item.get_text().replace("specialty", "")
            link = re.findall(link_pattern, item['onclick'])[0]

            absolute_link = self.getAbsLink(link)
            # absolute_link = "http://" + urljoin(self.parsed_url.scheme, self.parsed_url.netloc) + "/" + link # whatever man

            data = {
                'idx': idx,
                'name': name, 
                'link': absolute_link}
            
            idx += 1
            res.append(data)

        # Puts it somewhere
        # fn = "index"
        return Scraper.save(fn, res)

    def loadjson(fn='index.json'):
        with open(fn, 'r') as file:
            data = json.load(file)
        
        return data

    def scrapeIndex(self, folder_name="ingredients"):
        """Creates `/ingredients`
        
        Scrapes based on index.json
        
        Returns location of the folder"""
        num_of_files = 0

        if (os.path.exists("index.json")):
            indexes = Scraper.loadjson("index.json")
        else:
            self.makeIndex()

        res = []

        for note in indexes:
            link = note['link']
            name = note['name']
            idx = note['idx']
            iidx = 1

            # print(name, link)
            soup = self.scrape(link).find_all("td", class_="wrd80")

            for td in soup:
                ingr_link = td.find('a').get('href')
                raw_text = td.get_text() # TODO: fix trailing whitespace

                if (raw_text.find("FR") == False):
                    print(raw_text, " is NOT a fragrance, skipped")
                    break
                
                else:
                    ingr_name = re.sub(r'(FR)|(FL)|(\/)', "", raw_text)

                res.append({
                    'idx': iidx,
                    'ingr_name': ingr_name,
                    'ingr_link': ingr_link
                })

                iidx += 1

            
            Scraper.save(str(idx), res, folder_name)
            num_of_files += 1
            print("[LOG]: Saved <<", name, ">> to /ingredients as ", num_of_files, ".json")

            res.clear()

            time.sleep(4) # optional ..... i'm just being nice
        
        return folder_name

    def saveProfiles(self):
        """Creates `/profiles`
        
        
        Based on the fragrance
        
        1. Saves ingredients' profile 
        2. and words associated with notes on this profile
        
        file name = `ingredients.name`
        name = molecule/ingredient name
        cas = cas number # NOTE: unique and important
        jsmol = link to cool molecule simulator
        adj = any RELEVANT adjectives used to describe the molecule


        # NOTE: not implemented
        #         blenders = idxes that point back to ingredients/profiles?
        """

        if (not (os.path.exists('/ingredients') and os.len(os.listdir('/ingredients')) != 0)):
            raise Exception("/ingredients does not exist, run saveIndex() to create /ingredients")
        else:
            # igds = ingredients
            igds = os.listdir("/ingredients")

        for profile in igds:
            fn = self.saveOneProfile(profile)

    def saveOneProfile(self, fn_ingredient:str) -> str:
        if (not fn_ingredient.endswith(".json")):
            fn_ingredient += ".json"
            # hmm... haha

        data = Scraper.loadjson(fn_ingredient)
        link = data['link']
        soup = self.scrape(link)
        
        # link = re.findall(link_pattern, item['onclick'])[0]
        cas_pattern = r'CAS.*html'
        cas = soup.find_all("td", class_="radw8") # cas number


        # file name = `ingredients.name`
        # name = molecule/ingredient name
        # cas = cas number # NOTE: unique and important
        # jsmol = link to cool molecule simulator
        # adj = any RELEVANT adjectives used to describe the molecule







if __name__ == "__main__":
    url = "https://www.thegoodscentscompany.com/peb-az.html"
    s = Scraper(url)

    if (os.path.exists("index.json") == False):
        print("[LOG]: index.json does not exist, building index.json")
        fn_index = s.makeIndex()
    
    else:
        print("[LOG]: index.json exists, building ingredient list...")

    s.scrapeIndex()

    