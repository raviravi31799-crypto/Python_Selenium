from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/alerts")
wait=WebDriverWait(driver,10)
driver.find_element(By.XPATH,"//button[@id='alertButton']").click()
try:
    alert=driver.switch_to.alert
    alert.accept()
    print("Alert accepted succesfully")
except:
    print("No alert is present")
driver.find_element(By.XPATH,"//button[@id='confirmButton']").click()
try:
    alert=driver.switch_to.alert
    text=alert.text
    alert.dismiss()
    result= driver.find_element(By.XPATH,"//span[@id='confirmResult']").text
    print(text)
    print(result," Confirmation alert dismissed successfully")
except:
    print("No confiramtion alert")
element=driver.find_element(By.XPATH,"//button[@id='promtButton']").click()
alert=wait.until(EC.alert_is_present())

alert.send_keys("Joshni")
alerttext=alert.text
alert.accept()
promptresult=driver.find_element(By.XPATH,"//span[@id='promptResult']").text
print(promptresult)
print(alerttext,"Prompt alert is accepted")

element=driver.find_element(By.XPATH,"//button[@id='timerAlertButton']").click()
alert=wait.until(EC.alert_is_present())
text=alert.text
alert.accept()
print(text ,"Alert handled successfully using wait")




    





