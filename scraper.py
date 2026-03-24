import time # being nice <3
import requests
import re
from bs4 import BeautifulSoup

def scrape(site_url):
    """A simple scraper"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    profile_links = soup.find_all('a')

    for link in profile_links:
        print(link)
    
    time.sleep(4)


if __name__ == '__main__':
    url = 'https://www.thegoodscentscompany.com/peb-az.html'
    scrape(url)