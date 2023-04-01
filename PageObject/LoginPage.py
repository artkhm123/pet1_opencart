from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage
import time


class LoginPage(BasePage):
    CONTENT = (By.CSS_SELECTOR, "#content")
    H1_TITLE = (By.CSS_SELECTOR, "h1.panel-title")
    USERDATA_ALLERT = (By.CSS_SELECTOR, ".alert.alert-danger.alert-dismissible")
    USERNAME = (By.CSS_SELECTOR, "#input-username")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button[type=submit]")

    def h1_page_title(self):
        return self.get_text(self.H1_TITLE)

    def wrong_userdata_message(self):
        return self.get_text(self.USERDATA_ALLERT)

    def wrong_userdata_message_is_present(self):
        # элемент по дефолту отсутствует
        if len(self.driver.find_elements(*self.USERDATA_ALLERT)) == 0:
            return False
        else:
            return True

    def input_username(self, text):
        self.input_(self.USERNAME, text)

    def input_password(self, text):
        self.input_(self.PASSWORD, text)

    def login(self):
        self.click_(self.BUTTON_LOGIN)
        time.sleep(0.5)
