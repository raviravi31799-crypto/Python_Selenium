import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def test_setup_and_teardown():
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")
    yield
    driver.quit()

def test_validsearch(test_setup_and_teardown):
    driver.find_element(By.NAME,"search").send_keys("Mac")
    driver.find_element(By.CLASS_NAME,"btn.btn-default btn-lg").click()
    assert driver.find_element(By.XPATH,"//a[normalize-space()='iMac']").is_displayed()

def test_invalidsearch(test_setup_and_teardown):
    driver.find_element(By.NAME,"search").send_keys("Pen")
    driver.find_element(By.CLASS_NAME,"btn.btn-default btn-lg").click()
    expected="There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").__eq__(expected)

def test_nosearch(test_setup_and_teardown):
     driver.find_element(By.NAME,"search").send_keys("Pen")
     driver.find_element(By.CLASS_NAME,"btn.btn-default btn-lg").click()
     expected="There is no product that matches the search criteria."
     assert driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").__eq__(expected)

