import time # being nice <3
import requests
import re
from bs4 import BeautifulSoup

def scrape(site_url):
    """A simple scraper"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Selects
    pattern = r'data.*html'
    on_clicks = soup.find_all('a', {'onclick' : re.compile(pattern)})

    for item in on_clicks:
        print (re.findall(pattern, item['onclick'])[0], item.get_text())

    time.sleep(4)


if __name__ == '__main__':
    url = 'https://www.thegoodscentscompany.com/peb-az.html'
    scrape(url)