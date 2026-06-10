import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utility import read_config
from Utility import Logcreator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class searchpage:
    def __init__(self,driver):
        self.driver=driver
    search ="search"
    btn="btn.btn-default.btn-lg"
    result="//a[normalize-space()='iMac']"
    
    log=Logcreator.log_generator()
    def searchbar(self):
        keyword=read_config.get_config("search term","product")
        self.driver.find_element(By.NAME,self.search).send_keys(keyword)
    def click_search(self):
        self.driver.find_element(By.CLASS_NAME,self.btn).click()
    def check_result(self):
        product=self.driver.find_element(By.XPATH,self.result)
        assert product.is_displayed(),"Search is invalid"
        self.log.info("Search is successful")
