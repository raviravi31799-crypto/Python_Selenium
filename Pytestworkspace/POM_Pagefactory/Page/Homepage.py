from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from Utility import read_config
from Utility import Logcreator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Homepage(PageFactory):
 def __init__(self,driver):
   self.driver=driver
 



 locators={"accountlink":("xpath","//span[text()='My Account']"),
           "login":("xpath","//a[text()='Login']"),
           "username":("xpath","//input[@id='input-email']"),
    "password":("xpath","//input[@id='input-password']"),
    "login_btn":("xpath","//input[@value='Login']"),
    "logout":("xpath","//a[text()='Order History']/following::a[3]")}
 
log=Logcreator.log_generator() 
def Myaccount(self):   
        self.accountlink.click()
def click_login(self):
          
        element=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.login)))
        element.click()
        self.log.info("Clicked on Login link")
def enter_credentials(self):
        uname=read_config.get_config("Login data","username")
        self.username.send_keys(uname)
        self.log.info("Entered username")
        password=read_config.get_config("Login data","password")
        self.password.send_keys(password)
        self.log.info("Entered password")
def click_loginbutton(self):
        self.login_btn.click()
        
def logout_visible(self):
        logoutlink=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.logout)))
        assert logoutlink.is_displayed(),"Logout failed"
        self.log.info("Login successful")