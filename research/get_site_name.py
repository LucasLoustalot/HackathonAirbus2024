import requests
from bs4 import BeautifulSoup

def get_all_url(source_code):
    soup = BeautifulSoup(source_code, 'html.parser')

    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    return urls
