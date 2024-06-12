from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import extract.json_to_csv
import research.getURLs as getURLs
import interface.translate
import research.deleteDuplicates
#import extract.gemini

def search(keyWord : str, countryCode : str, language : str) -> list[str] :
    option = webdriver.ChromeOptions()
    option.add_argument("--headless=new")

    driver = webdriver.Chrome(options=option)

    translatedProduct = interface.translate.translated_text(keyWord, "auto", language).replace(" ", "+")
    product = keyWord.replace(" ", "+")

    url = "https://www.google.com/search?as_q=" + translatedProduct + "&as_epq=&as_oq=&as_eq=&as_nlo=&as_nhi=&lr=&cr=country" + countryCode + "&as_qdr=all&as_sitesearch=&as_occt=any&as_filetype=&tbs="

    driver.get(url)

    companyName = getURLs.getAllURLs(driver.page_source)

    url = "https://www.google.com/search?as_q=" + product + "&as_epq=&as_oq=&as_eq=&as_nlo=&as_nhi=&lr=&cr=country" + countryCode + "&as_qdr=all&as_sitesearch=&as_occt=any&as_filetype=&tbs="

    driver.get(url)

    companyName = companyName + getURLs.getAllURLs(driver.page_source)

    filteredName = research.deleteDuplicates.deleteDuplicates(companyName)

    driver.close()

    resultList = []

    for companyUrl in filteredName:
        json = extract.gemini.get_company_data(companyUrl)
        if ("args" not in json):
            resultList.append(";;" + companyUrl + ";;;;;;;")
            continue
        csv = extract.json_to_csv.json_to_csv(json)
        resultList.append(csv)

    return resultList


