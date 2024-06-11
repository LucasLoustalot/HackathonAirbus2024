from selenium import webdriver
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_argument("--headless=new")

driver = webdriver.Chrome(options=option)

driver.get("https://www.google.com/search?q=clamps+company")

print(driver.title)

driver.close()
