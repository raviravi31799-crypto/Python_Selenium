from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.leafground.com/")
wait=WebDriverWait(driver,10)
element=wait.until(EC.visibility_of_element_located((By.XPATH,"//i[@class='pi pi-server layout-menuitem-icon']"))).click()
dropdown=driver.find_element(By.XPATH,"//span[text()='Dropdown']").click()
values=driver.find_element(By.XPATH,"//select[@class='ui-selectonemenu']")
select=Select(values)
select.select_by_visible_text("Selenium")
print("selected by index")
time.sleep(5)
select.select_by_index(1)
print("selected by visible index")





