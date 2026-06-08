from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")
driver.find_element(By.XPATH,"//i[@class='fa fa-envelope']/parent::a").click()
assert driver.find_element(By.XPATH,"//div[@class='contact-form']/child::h2").is_displayed()
print("Contactus Form is opened")
driver.find_element(By.XPATH,"//input[@data-qa='name']").send_keys("John")
driver.find_element(By.XPATH,"//input[@data-qa='email']").send_keys("John@gmail.com")
driver.find_element(By.XPATH,"//input[@data-qa='subject']").send_keys("Regarding the products quality")
driver.find_element(By.XPATH,"//textarea[@data-qa='message']").send_keys("The products are really good and highly maintainable")
driver.find_element(By.XPATH,"//input[@name='submit']").click()
alert=driver.switch_to.alert
alert.accept()
msg=driver.find_element(By.XPATH,"//div[@class='status alert alert-success']").text
print(msg)
print("Form filled successfully")