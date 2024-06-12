from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import get_site_name

def search(keyWord : str, countryCode : str, language : str) :
    option = webdriver.ChromeOptions()
    option.add_argument("--headless=new")

    driver = webdriver.Chrome(options=option)

    product = keyWord.replace(" ", "+")

    url = "https://www.google.com/search?as_q=" + product + "&as_epq=&as_oq=&as_eq=&as_nlo=&as_nhi=&lr=&cr=country" + countryCode + "&as_qdr=all&as_sitesearch=&as_occt=any&as_filetype=&tbs="

    driver.get(url)

    companyName = get_site_name.get_all_url(driver.page_source)

    driver.close()
