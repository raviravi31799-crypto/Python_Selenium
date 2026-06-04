import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.maximize_window()
url="https://www.google.co.in"
driver.get(url)
print(driver.title)
driver.find_element(By.NAME,value='q').is_enabled()
driver.find_element(By.NAME,value='q').send_keys("Selenium")
time.sleep(5)
Search=driver.find_element(By.NAME,value='q')
Search(Keys.ENTER)
driver.find_element(By.NAME,value="btnK").is_enabled()
time.sleep(5)
driver.find_element(By.NAME,value="btnK").click()
driver.close()


