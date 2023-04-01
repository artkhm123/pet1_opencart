import time
from selenium.webdriver.common.by import By

from PageObject.BasePage import BasePage


class HeaderElement(BasePage):
    CURRENCY_BTN = (By.CSS_SELECTOR, "button[class='btn btn-link dropdown-toggle']")
    USD = (By.CSS_SELECTOR, "button[name='USD']")
    EUR = (By.CSS_SELECTOR, "button[name='EUR']")
    GBP = (By.CSS_SELECTOR, "button[name='GBP']")
    LOGOUT_FROM_ADMIN_PAGE = (By.CSS_SELECTOR, "#header > div > ul > li:nth-child(2) > a > span")
    USER_DROPDOWN = (By.CSS_SELECTOR, "#header > div > ul > li.dropdown > a")
    THIS = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver):
        super().__init__(driver=driver)

    @property
    def choose_USD(self):
        self.click_(self.USD)

    def change_currency_to(self, currency: str):
        time.sleep(0.5)
        self.click_(self.CURRENCY_BTN)
        time.sleep(0.5)
        if currency == "USD":
            self.click_(self.USD)
        if currency == "EUR":
            self.click_(self.EUR)
        if currency == "GBP":
            self.click_(self.GBP)

    def logout_btn(self):
        time.sleep(0.5)
        return self.element(self.LOGOUT_FROM_ADMIN_PAGE)

    def logout_from_admin_panel(self):
        time.sleep(0.5)
        self.click_(self.LOGOUT_FROM_ADMIN_PAGE)

    @property
    def user_name(self):
        return self.get_text(self.USER_DROPDOWN)
