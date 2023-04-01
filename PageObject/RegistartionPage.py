from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time


class RegistartionPage(BasePage):
    H1_TITLE = (By.CSS_SELECTOR, "#content > h1")
    FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    ACCOUNT_FRAIM = (By.CSS_SELECTOR, "#account-register")
    MODAL_TITLE = (By.CSS_SELECTOR, "h4.modal-title")
    CLOSE_BTN = (By.CSS_SELECTOR, "button.close")
    PRIVATE_POLICY_CHECKBOX = (By.CSS_SELECTOR, "input[type=checkbox]")
    CONTINUE_BTN = (By.CSS_SELECTOR, "input[value=Continue]")

    def h1_title(self):
        return self.get_text(self.H1_TITLE)

    def title_font_color(self):
        return self.driver.element(self.H1_TITLE).value_of_css_property("color")

    def title_font_size(self):
        title = self.element(self.H1_TITLE)
        return int(title.value_of_css_property("font-size").replace('px', ''))

    def input_firstname(self, text):
        self.input_(self.FIRSTNAME, text)

    def input_lastname(self, text):
        self.input_(self.LASTNAME, text)

    def input_email(self, text):
        self.input_(self.EMAIL, text)

    def input_phone(self, text):
        self.input_(self.TELEPHONE, text)

    def input_password(self, text):
        self.input_(self.PASSWORD, text)

    def confirm_password(self, text):
        self.input_(self.PASSWORD_CONFIRM, text)

    def open_private_policy_modal_window(self):
        account_reg_form = self.element(self.ACCOUNT_FRAIM)
        account_reg_form.find_element(By.LINK_TEXT, "Privacy Policy").click()

    def private_policy_modal_window_title(self):
        return self.get_text(self.MODAL_TITLE)

    def close_private_policy_modal_window(self):
        self.click_(self.CLOSE_BTN)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body[class='']")))

    def confirm_private_policy_agreement(self):
        self.click_(self.PRIVATE_POLICY_CHECKBOX)

    def confirm_registration(self):
        time.sleep(0.5)
        self.click_(self.CONTINUE_BTN)
