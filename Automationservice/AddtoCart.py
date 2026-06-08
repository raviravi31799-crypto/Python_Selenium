from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com")
def dismiss_ads(driver):
    try:
        driver.execute_script("""
            var iframes = document.querySelectorAll('iframe');
            for (var i = 0; i < iframes.length; i++) {
                var src = iframes[i].src || '';
                var id  = iframes[i].id  || '';
                if (
                    src.includes('doubleclick') ||
                    src.includes('googleads')   ||
                    src.includes('googlesyndication') ||
                    id.includes('aswift')       ||
                    id.includes('google_ads')
                ) {
                    iframes[i].remove();
                }
            }
        """)
        print("Ads dismissed")
    except Exception as e:
        print(f"Ad dismissal skipped: {e}")
dismiss_ads(driver)

wait=WebDriverWait(driver,15)
home=wait.until(EC.visibility_of_element_located((By.XPATH,"//i[@class='fa fa-home']/parent::a")))
assert home.is_displayed(),"Home page is not displayed"
print("Home page is displayed")
wait.until(EC.visibility_of_element_located((By.XPATH,"//i[@class='material-icons card_travel']/parent::a"))).click()
dismiss_ads(driver)
action=ActionChains(driver)
product1=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='single-products']/child::div")))
action.scroll_to_element(product1)
action.move_to_element(product1).perform()
print("Moved to element")
cart=wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@data-product-id='1']//ancestor::div[@class='overlay-content']")))
action.move_to_element(cart).click()
Addmsg=driver.find_element(By.XPATH,"//h4[@class='modal-title w-100']")
if Addmsg.is_displayed:
    print("Product added to cart successfully")
else:
    print("Add to cart failed")
wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@data-dismiss='modal']"))).click()
product2=driver.find_element(By.XPATH,"//div[@class='single-products']/following::a[2]")
action.move_to_element(product2).perform()
#driver.find_element(By.XPATH,"//i[@class='fa fa-shopping-cart'][2]").click()
