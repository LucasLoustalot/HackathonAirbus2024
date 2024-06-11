import requests
from bs4 import BeautifulSoup

ban_words = [
    "amazon",
    "manomano",
    "linkedin",
    "alibaba",
    "metoree",
    "google",
    "ebay"
]

def get_all_url(source_code: str) -> list[str]:
    soup = BeautifulSoup(source_code, 'html.parser')

    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    return urls
