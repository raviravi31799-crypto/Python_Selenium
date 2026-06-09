import pytest
import read_config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login(self):
        wait=WebDriverWait(self.driver,5)
        self.driver.find_element(By.XPATH,"//a[@id='login2']").click()
        uname=read_config.get_config("Login data","username")
        Pass=read_config.get_config("Login data","password")
        
        self.driver.wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='loginusername']"))).sendkeys(uname)
        self.driver.wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='loginpassword']"))).sendkeys(Pass)
        self.driver.wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@onclick='logIn()']"))).click()
        assert self.driver.wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@onclick='logOut()']"))).is_displayed()
        print("Login successful")
