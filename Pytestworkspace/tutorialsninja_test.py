import pytest
# from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")

class TestSearch:
    @pytest.mark.order(1)
    def test_validsearch(self):
        self.driver.find_element(By.NAME,"search").send_keys("Mac")
        self.driver.find_element(By.CLASS_NAME,"btn.btn-default.btn-lg").click()
        assert self.driver.find_element(By.XPATH,"//a[normalize-space()='iMac']").is_displayed()

    @pytest.mark.order(3)
    def test_invalidsearch(self):
        self.driver.find_element(By.NAME,"search").send_keys("Pen")
        self.driver.find_element(By.CLASS_NAME,"btn.btn-default.btn-lg").click()
        expected="There is no product that matches the search criteria."
        actual= self.driver.find_element(By.XPATH,"//p[text()='There is no product that matches the search criteria.']").text
        assert actual==expected

     
    @pytest.mark.order(2)
    def test_nosearch(self):
       self.driver.find_element(By.NAME,"search").send_keys(" ")
       self.driver.find_element(By.CLASS_NAME,"btn.btn-default.btn-lg").click()
       expected="There is no product that matches the search criteria."
       actual=self.driver.find_element(By.XPATH,"//p[text()='There is no product that matches the search criteria.']").text
       assert actual==expected

