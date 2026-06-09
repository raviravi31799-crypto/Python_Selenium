import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import read_config

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_validsearch(self):
       
        search= self.driver.find_element(By.NAME,"search")
        keyword=read_config.get_config("search term","validterm")
        search.send_keys(keyword)
        self.driver.find_element(By.CLASS_NAME,"btn.btn-default.btn-lg").click()
        assert self.driver.find_element(By.XPATH,"//a[normalize-space()='iMac']").is_displayed()

    def test_invalidsearch(self):
       
        search=self.driver.find_element(By.NAME,"search")
        invalid=read_config.get_config("search term","Invalidterm")
        search.send_keys(invalid)
        self.driver.find_element(By.CLASS_NAME,"btn.btn-default.btn-lg").click()
        expected="There is no product that matches the search criteria."
        actual= self.driver.find_element(By.XPATH,"//p[text()='There is no product that matches the search criteria.']").text
        assert actual==expected