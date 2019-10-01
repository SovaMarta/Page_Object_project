from selenium.common.exceptions import NoAlertPresentException # в начале файла

def solve_quiz_and_get_code(self):
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")
        
from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_check()


def test_should_be_add_to_basket_button(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()


def test_should_be_message_success_add_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_click()
    page.should_be_message_success_add_to_basket()


def test_should_be_product_price_add_to_basket_price(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_price_add_to_basket_price()


def test_get_product_price(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_click()
    page.get_product_price()


def test_get_current_basket_value(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_click()
    page.get_current_basket_value()        
        
