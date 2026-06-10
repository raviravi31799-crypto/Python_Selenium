import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utility import read_config
from Utility import Logcreator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Homepage:
    def __init__(self,driver):
        self.driver=driver
    
    account="//span[text()='My Account']"
    login="//a[text()='Login']"
    username="//input[@id='input-email']"
    password="//input[@id='input-password']"
    login_btn="//input[@value='Login']"
    logout="//a[text()='Order History']/following::a[3]"
     
    log=Logcreator.log_generator() 
    def click_account(self):   
        acc=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.account)))
        acc.click()
    def click_login(self):
          
        element=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.login)))
        element.click()
        self.log.info("Clicked on Login link")
    def enter_credentials(self):
        uname=read_config.get_config("Login data","username")
        self.driver.find_element(By.XPATH,self.username).send_keys(uname)
        self.log.info("Entered username")
        password=read_config.get_config("Login data","password")
        self.driver.find_element(By.XPATH,self.password).send_keys(password)
        self.log.info("Entered password")
    def click_loginbutton(self):
        self.driver.find_element(By.XPATH,self.login_btn).click()
        
    def logout_visible(self):
        logoutlink=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.logout)))
        assert logoutlink.is_displayed(),"Logout failed"
        self.log.info("Login successful")


       