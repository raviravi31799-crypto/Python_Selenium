import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
url="https://www.google.co.in"
driver.get(url)
print(driver.title)
time.sleep(5)
driver.close()