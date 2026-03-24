import time # being nice <3
import requests
from bs4 import BeautifulSoup

def scrape(site_url):
    """A simple scraper"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    time.sleep(4)

    return soup

def parse(soup:BeautifulSoup):
    fragbase = soup.select('td > *')
    fragbase = soup.select()


    for item in parsed:
        print (item)

# Use(s): fragrance agents</td>, <td><a href="#" onclick="openMainWindow('/data/pb1114361.html');return false;">amber woody specialty</a>

if __name__ == '__main__':
    url = 'https://www.thegoodscentscompany.com/peb-az.html'
    soup = scrape(url)
    parse(soup)