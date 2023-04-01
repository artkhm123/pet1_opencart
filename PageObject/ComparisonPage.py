from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage


class ComparisonPage(BasePage):
    PRODUCT1 = (
        By.CSS_SELECTOR, "#content > table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)")
    PRODUCT2 = (
        By.CSS_SELECTOR, "#content > table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)")

    PRODUCT3 = (
        By.CSS_SELECTOR, "#content > table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(4)")
    PRODUCT4 = (
        By.CSS_SELECTOR, "#content > table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5)")

    def comparison_product_name(self, number):
        if number == 1:
            return self.get_text(self.PRODUCT2)
        elif number == 2:
            return self.get_text(self.PRODUCT3)
        elif number == 3:
            return self.get_text(self.PRODUCT4)
        else:
            return self.get_text(self.PRODUCT1)
