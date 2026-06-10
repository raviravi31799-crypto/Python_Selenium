import pytest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import excelReader
from Utilities import logCreator

@pytest.mark.parametrize("username,password",excelReader.get_data(r"D:\\Python\\PythonSelenium\\Pytestworkspace\\DataDriven_Excel\\ExcelFiles\\Logindata.xlsx","Tutorialsninja"))
class Testlogin:
    log=logCreator.log_generator()
    def test_validlogin(self,username,password):
        self.driver=webdriver.Chrome()
        self.log.info("Instantiating browser")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://tutorialsninja.com/demo/")
        self.log.info("Application launched successfully")
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu.dropdown-menu-right']//a[text()='Login']").click()
        self.driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys(username)
        self.log.info("Entered username")
        self.driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys(password)
        self.log.info("Entered password")
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
       
        self.log.info("Login successful")
        self.driver.quit()
    

    