import selenium
import time,os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
driver = None
options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1080')
options.add_argument("--disable-notifications")
options.add_argument('--disable-gpu')
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
driver = webdriver.Chrome('chromedriver', options=options)
driver.get('https://mostaql.com/projects')
jobs = driver.find_elements(By.XPATH, "//h2[@class='mrg--bt-reset']//a")

title = jobs[0].text
link = jobs[0].get_attribute('href')

jobs[0].click()
description = driver.find_element(By.CLASS_NAME, "carda__content").text
budget = driver.find_element(By.XPATH, '//*[@id="project-meta-panel"]/div[1]/table/tbody/tr[3]/td[2]/span').text
allinf = [title,link,description,budget]
driver.quite()
