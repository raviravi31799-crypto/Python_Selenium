import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By 

@pytest.mark.parametrize("Browsers",[('Chrome'),('Firefox')])
@pytest.mark.parametrize("input_url",[("https://www.google.co.in/"),("https://www.flipkart.com/")])
def test_parameters(Browsers,input_url):
    if Browsers=="Chrome":
        driver=webdriver.Chrome()
    if Browsers=="Firefox":
        driver=webdriver.Firefox()
    driver.maximize_window()
    driver.get(input_url)
    print(driver.title)
    time.sleep(5)
    driver.close()

     