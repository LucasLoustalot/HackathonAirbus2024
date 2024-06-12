from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import research.getURLs as getURLs
import interface.translate
import research.deleteDuplicates

def search(keyWord : str, countryCode : str, language : str) -> list[str] :
    option = webdriver.ChromeOptions()
    option.add_argument("--headless=new")

    driver = webdriver.Chrome(options=option)

    product = interface.translate.translated_text(keyWord, "auto", language).replace(" ", "+")

    url = "https://www.google.com/search?as_q=" + product + "&as_epq=&as_oq=&as_eq=&as_nlo=&as_nhi=&lr=&cr=country" + countryCode + "&as_qdr=all&as_sitesearch=&as_occt=any&as_filetype=&tbs="

    driver.get(url)

    companyName = getURLs.getAllURLs(driver.page_source)

    filteredName = research.deleteDuplicates.deleteDuplicates(companyName)

    driver.close()

    return [
            "Airbus; Toulouse; https://www.airbus.com/fr/airbus-atlantic; support@airbus.com; 100M; 100K; FR; Skil; Aviation; Army",
            "name2; location2; link2; contact2; revenue2; size2; Airbus.com; skills2; main domain2; main customers2",
        ]
