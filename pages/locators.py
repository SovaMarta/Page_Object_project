from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
    
class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "[value = 'Log In']")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "[value = 'Register']")

class ProductPageLocators(object):
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main > p.price_color")
    BASKET_PRODUCT = (By.CSS_SELECTOR, ".btn-add-to-basket")
    
