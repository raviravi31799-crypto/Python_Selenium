import pytest
from selenium import webdriver
from Page.Homepage import Homepage

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    
    def test_flow(self):
        homepage=Homepage(self.driver)
        homepage.Myaccount()
        homepage.click_login()
        homepage.enter_credentials()
        homepage.click_loginbutton()
        homepage.click_account()
        homepage.logout_visible()