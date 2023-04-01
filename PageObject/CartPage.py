from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage


class CartPage(BasePage):
    PRODUCT1_NAME = (
        By.CSS_SELECTOR, "#content > form > div > table > tbody > tr > td:nth-child(2) > a")
    PRODUCT1_QTY = (By.CSS_SELECTOR, "#content > form > div > table > tbody > tr > td:nth-child(4) > div > input")
    PRODUCT1_PRICE = (By.CSS_SELECTOR, "#content > form > div > table > tbody > tr > td:nth-child(5)")
    REMOVE_FIRST_PRODUCT_BTN = (By.CSS_SELECTOR, "button[data-original-title='Remove']")

    def product_in_cart_name(self):
        return self.get_text(self.PRODUCT1_NAME)

    def product_in_cart_qty(self):
        return int(self.element(self.PRODUCT1_QTY).get_attribute("value"))

    def product_in_cart_price(self):
        return float(self.get_text(self.PRODUCT1_PRICE).replace('$', ''))

    def remove_product(self):
        self.click_(self.REMOVE_FIRST_PRODUCT_BTN)
