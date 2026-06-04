import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.maximize_window()
url="http://automationexercise.com"
driver.get(url)
driver.find_element(By.XPATH,"//a[@href='/login']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//h2[text()='New User Signup!']']").is_displayed()
Email=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@data-qa='signup-name']"))).send_keys("Joshvi")
driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys("jo28@gmail.com")
driver.find_element(By.XPATH,"//button[@data-qa='signup-button']").click()


driver.find_element(By.XPATH,"//b[text()='Enter Account Information']").is_displayed()
driver.find_element(By.ID,value="id_gender2").click()
driver.find_element(By.ID,value="password").send_keys("123456")
day=driver.find_element(By.ID,value="days")
day.select_by_visible_text("28")
month=driver.find_element(By.ID,value="months")
month.select_by_visible_text("May")
driver.find_element(By.ID,value="years").select_by_visible_text("2005")
driver.find_element(By.ID,value="newsletter").click()
driver.find_element(By.ID,value="optin").click()
driver.find_element(By.ID,value="first_name").send_keys("Joshvini")
driver.find_element(By.ID,value="last_name").send_keys("Ram")
driver.find_element(By.ID,value="address1").send_keys("Ramvilas")
driver.find_elemdriverent(By.ID,value="state").send_keys("TamilNadu")
driver.find_element(By.ID,value="city").send_keys("Madurai")
driver.find_element(By.ID,value="zipcode").send_keys("636211")
driver.find_element(By.ID,value="mobile_number").send_keys("9080706050")
driver.find_element(By.XPATH,"//button[@data-qa='create-account']").click()

driver.find_element(By.XPATH,"//h2[@data-qa='account-created']").is_displayed()
driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()
driver.find_element(By.XPATH,"//a[text()=' Logged in as ']").text
driver.find_element(By.XPATH,"//a[text()='  Delete Account']").click()
driver.find_element(By.XPATH,"//h2[@data-qa='account-deleted']").is_displayed()
driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()
