import requests
from bs4 import BeautifulSoup

ban_words = [
    "amazon",
    "manomano",
    "linkedin",
    "alibaba",
    "metoree",
    "google",
    "ebay",
    "wiki",
    "etsy",
    "indeed",
    "temu",
    "youtube",
    "grainger",
    "sonepar",
    "hdsupply",
    "aliexpress",
    "porn",
    "facebook",
    "xxx",
    "nazi",
    "fuck",
    "racist",
    "homedepot",
]

def getHomePage(url: str) -> str:
    homePage = ""
    i = 0
    while url[i] != '/':
        homePage += url[i]
        i += 1
    homePage += url[i]
    i += 1
    homePage += url[i]
    i += 1
    while url[i] != '/':
        homePage += url[i]
        i += 1
    return homePage

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
            urls.append(getHomePage(url))
    return urls

print(getHomePage('https://www.cejn.com/fr-fr/marches/hydrogene/'))