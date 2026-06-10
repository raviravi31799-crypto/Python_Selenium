import pytest
from selenium import webdriver
from Pages.Homepage import Homepage
from Pages.Searchpage import searchpage

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    
    def test_flow(self):
        homepage=Homepage(self.driver)
        homepage.click_account()
        homepage.click_login()
        homepage.enter_credentials()
        homepage.click_loginbutton()
        homepage.click_account()
        homepage.logout_visible()
        search=searchpage(self.driver)
        search.searchbar()
        search.click_search()
        search.check_result()