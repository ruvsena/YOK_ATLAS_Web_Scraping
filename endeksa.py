from tkinter import Image
import base64
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup, Comment


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
driver_path = r"C:\\Users\\pc\\Desktop\\chromedriver.exe"
chrome_service = Service(driver_path)
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
browser =webdriver.Chrome(service=chrome_service, options=chrome_options)


browser.get("https://www.endeksa.com/tr/analiz/turkiye/istanbul/silivri/demografi")
wait = WebDriverWait(browser, 4)
sleep(100)
element= browser.find_element(By.CLASS_NAME,'col-md-12')
#element = wait.until(EC.element_located_to_be_selected(
  # (By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div[1]/div/ui-view/div/section[1]/div[1]/div[1]/div/h1")))
browser.execute_script("window.scrollTo(0,50)")
location = element.location
size = element.size
browser.save_screenshot("due.png")
x = location['x']
y = location['y']
w = size['width']
h = size['height']
width = x + w
height = y + h
im = Image.open('due.png')
im = im.crop((int(x), int(y), int(width), int(height)))
im.save('due.png')
sleep(5)
