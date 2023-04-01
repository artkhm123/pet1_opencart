from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage


class MainPage(BasePage):
    TUMB_LIST = (By.CSS_SELECTOR, ".product-thumb.transition")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[onclick*='cart']")
    ADD_TO_WISHLIST_BTN = (By.CSS_SELECTOR, "button[onclick*='wishlist']")
    CAMPARE_BTN = (By.CSS_SELECTOR, "button[onclick*='compare']")

    def tumb_list(self):
        return self.elements(self.TUMB_LIST)

    def tumb(self, tumb_number):
        return self.tumb_list()[tumb_number]

    def add_to_cart_button_is_present(self, tumb_number):
        return len(self.tumb(tumb_number).find_elements(By.CSS_SELECTOR, "button[onclick*='cart']")) > 0

    def add_to_wish_list_button_is_present(self, tumb_number):
        return len(self.tumb(tumb_number).find_elements(By.CSS_SELECTOR, "button[onclick*='wishlist']")) > 0

    def add_to_comparison_button_is_present(self, tumb_number):
        return len(self.tumb(tumb_number).find_elements(By.CSS_SELECTOR, "button[onclick*='compare']")) > 0

    def click_compare_this_product(self, tumb_number):
        product_name = self.tumb(tumb_number).find_element(By.CSS_SELECTOR, ".caption h4 a").text
        self.tumb(tumb_number).find_element(By.CSS_SELECTOR, "button[onclick*='compare']").click()
        return product_name

    def click_add_to_wishlist(self, tumb_number):
        product_name = self.tumb(tumb_number).find_element(By.CSS_SELECTOR, ".caption h4 a").text
        self.tumb(tumb_number).find_element(By.CSS_SELECTOR, "button[onclick*='wishlist']").click()
        return product_name
