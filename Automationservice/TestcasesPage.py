from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://automationexercise.com')
wait=WebDriverWait(driver,15)
home=wait.until(EC.visibility_of_element_located((By.XPATH,"//i[@class='fa fa-home']/parent::a")))
assert home.is_displayed(),"Home page is not displayed"
print("Home page is displayed")
testcasepage=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='col-sm-12']/descendant::button[1]"))).click()
word=driver.find_element(By.XPATH,"//div[@class='row']/descendant::h2[1]")
assert word.is_displayed(),"Navigation is unsuccessful"
print("Navigated to test cases page")

