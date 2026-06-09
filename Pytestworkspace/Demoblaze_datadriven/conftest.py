import pytest
from selenium import webdriver
import read_config

@pytest.fixture()
def setup_and_teardown(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    url=read_config.get_config("Requirements","url")
    driver.get(url)
    request.cls.driver=driver
    yield 
    driver.quit()
    