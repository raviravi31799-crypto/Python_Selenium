from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https://automationexercise.com")
    wait=WebDriverWait(driver,15)
    home=wait.until(EC.visibility_of_element_located((By.XPATH,"//i[@class='fa fa-home']/parent::a")))
    assert home.is_displayed(),"Home page is not displayed"
    print("Home page is displayed")
except Exception as e:
    print("Test Failed:", e)

    driver.save_screenshot("failure.png")
    print("Screenshot saved as failure.png")

driver.find_element(By.XPATH,"//a[@href='/login']").click()
login=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='login-form']/child::h2")))
login.is_displayed(),"Form is not visible"
print("Proceed Login")
driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys("hy@gmail.com")
driver.find_element(By.XPATH,"//input[@data-qa='login-password']").send_keys("123456")
driver.find_element(By.XPATH,"//button[@data-qa='login-button']").click()
try:
    driver.find_element(By.XPATH,"//i[@class='fa fa-user']/parent::a").is_displayed()
    print("Login successful")
except Exception as e:
    print("Test Failed:", e)
    driver.save_screenshot("failed.png")
    print("Screenshot saved as failed.png")
driver.find_element(By.XPATH,"//i[@class='fa fa-trash-o']/parent::a").click()
deleted=driver.find_element(By.XPATH,"//h2[@data-qa='account-deleted']/child::b")
assert deleted.is_displayed(),"Unable to delete account"
print("valid login successful")


