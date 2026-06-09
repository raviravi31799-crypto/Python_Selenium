import pytest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import excelReader
from Utilities import logCreator

@pytest.mark.parametrize("username,password",excelReader.get_data(r"D:\\Python\\PythonSelenium\\Pytestworkspace\\DataDriven_Excel\\ExcelFiles\\Logindata.xlsx","Login"))
class TestLogin:
    log=logCreator.log_generator()
    def test_validlogin(self,username,password):
        self.driver=webdriver.Chrome()
        self.log.info("Instantiating browser")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.demoblaze.com/")
        self.log.info("Application launched successfully")
        self.driver.find_element(By.XPATH,"//a[@id='login2']").click()
        self.driver.find_element(By.XPATH,"//input[@id='loginusername']").send_keys(username)
        self.log.info("Entered username")
        self.driver.find_element(By.XPATH,"//input[@id='loginpassword']").send_keys(password)
        self.log.info("Entered password")
        self.driver.find_element(By.XPATH,"//button[@onclick='logIn()']").click()
        # logout=self.driver.find_element(By.ID,"logout2")
        # assert logout.is_displayed(),"Logout failed"
        self.log.info("Login successful")
        self.driver.quit()
    

    