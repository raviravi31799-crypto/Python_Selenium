from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
wait=WebDriverWait(driver,10)
phone=wait.until(EC.visibility_of_element_located((By.XPATH,"//i[contains(@class='fa-phone')]")))
driver.find_element(locate_with(By.XPATH,"//span[text()='My Account']")).to_right_of(phone).click()
register=driver.find_element(By.XPATH,"//a[text()='Register'][1]")
driver.find_element(locate_with(By.XPATH,"//a[text()='Login']")).below(register).click()
password=driver.find_element(By.XPATH,"//input[@id='input-password']")
username=driver.find_element(locate_with(By.XPATH,"//input[@id='input-email']")).above(password)
username.send_keys("jothika@gmail.com")
email=driver.find_element(By.XPATH,"//input[@id='input-email']")
Password=driver.find_element(locate_with(By.XPATH,"//input[@id='input-password']")).below(email)
Password.send_keys("admin5")
driver.find_element(locate_with(By.XPATH,"//input[@value='Login']")).below(password).click()
wishlist=driver.find_element(By.XPATH,"//i[@class='fa fa-heart']")
logout=driver.find_element(locate_with(By.XPATH,"//a[text()='Order History']/following::a[3]")).to_left_of(wishlist)
assert logout.is_displayed(),"Login failed"
print("Login successful")
driver.quit()








