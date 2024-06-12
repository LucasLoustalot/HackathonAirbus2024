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

def urlIsCorrect(url: str) -> bool:
    if len(url) < 8:
        return False
    if "https" not in url and "http" not in url:
        return False
    for word in ban_words:
        if word in url:
            return False
    return True

def getAllURLs(source_code: str) -> list[str]:
    soup = BeautifulSoup(source_code, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        url = str(link.get('href'))
        if urlIsCorrect(url):
            urls.append(link.get('href'))
    return urls

print(urlIsCorrect('None'))