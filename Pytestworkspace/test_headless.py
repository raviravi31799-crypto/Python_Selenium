import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

@pytest.mark.parametrize("Browsers",[('Chrome'),('Firefox')])
@pytest.mark.parametrize("input_url",[("https://www.google.co.in/"),("https://www.flipkart.com/")])
def test_parameters(Browsers,input_url):
    options=Options()
    if Browsers=="Chrome":
        driver=webdriver.Chrome(options=options)
        options.add_argument("headless=new")
    if Browsers=="Firefox":
        driver=webdriver.Firefox()
    driver.maximize_window()
    driver.get(input_url)
    print(driver.title)
    time.sleep(5)
    driver.close()

     
