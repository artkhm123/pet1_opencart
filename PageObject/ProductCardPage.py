import time

from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage


class ProductCardPage(BasePage):
    CART_COUNTER = (By.CSS_SELECTOR, "#cart-total")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > ul:nth-child(4) > li:nth-child(1) > h2")
    PRODUCT_QTY = (By.CSS_SELECTOR, "#input-quantity")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#button-cart")
    ADD_TO_CART_BTN2 = (By.CSS_SELECTOR, "button[onclick*='cart']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")

    def cart_counter(self):
        time.sleep(0.5)
        return self.get_text(self.CART_COUNTER)

    def get_product_price(self):
        return self.get_text(self.PRODUCT_PRICE)

    def product_qty(self):
        return int(self.element(self.PRODUCT_QTY).get_attribute("value"))

    def add_to_cart_btn_click(self):
        self.click_(self.ADD_TO_CART_BTN)

    def product_name(self):
        return self.get_text(self.PRODUCT_NAME)
