from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage


class AccountSuccessPage(BasePage):
    CONTENT = (By.CSS_SELECTOR, "#content")
    H1_TITLE = (By.CSS_SELECTOR, "#content > h1")
    CONTINUE = (By.LINK_TEXT, "Continue")

    def h1_title(self):
        return self.get_text(self.H1_TITLE)

    def continue_btn(self):
        return self.element(self.CONTINUE)
