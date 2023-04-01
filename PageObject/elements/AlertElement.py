import time
from selenium.webdriver.common.by import By

from PageObject.BasePage import BasePage


class AlertElement(BasePage):
    ALLERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    ALLERT_WARNING = (By.CSS_SELECTOR, ".alert-danger")
    COMPARISON = (By.LINK_TEXT, "product comparison")
    SHOPING_CART = (By.LINK_TEXT, "shopping cart")

    @property
    def success_alert_message_text(self):
        time.sleep(0.5)
        return self.get_text(self.ALLERT_SUCCESS)

    @property
    def warning_alert_message_text(self):
        time.sleep(0.5)
        return self.get_text(self.ALLERT_WARNING)

    @property
    def comparison_allert(self):
        time.sleep(0.5)
        return self.element(self.COMPARISON)

    @property
    def shoping_cart_allert(self):
        time.sleep(0.5)
        return self.element(self.SHOPING_CART)
