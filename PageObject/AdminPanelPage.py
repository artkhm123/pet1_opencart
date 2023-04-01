from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage


class AdminMainPage(BasePage):
    SIDE_MENU = (By.CSS_SELECTOR, "#menu")
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    CATALOG_PRODUCTS = (By.CSS_SELECTOR, "#menu-catalog > #collapse1 > li:nth-child(2)")
    H1_TITLE = (By.CSS_SELECTOR, "#content > div.page-header > div > h1")
    ADD_BTN = (By.CSS_SELECTOR, "a[data-original-title='Add New']")
    GENERAL_TAB = (By.LINK_TEXT, "General")
    DATA_TAB = (By.LINK_TEXT, "Data")
    LINKS_TAB = (By.LINK_TEXT, "Links")
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name1")
    PRODUCT_METADATA_INPUT = (By.CSS_SELECTOR, "#input-meta-title1")
    PRODUCT_MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")
    PRODUCT_PRICE_INPUT = (By.CSS_SELECTOR, "#input-price")
    PRODUCT_QTY_INPUT = (By.CSS_SELECTOR, "#input-quantity")
    SAVE_BTN = (By.CSS_SELECTOR, "button[data-original-title='Save']")
    FILTER_BY_NAME_INPUT = (By.CSS_SELECTOR, "#input-name")
    FILTER_SUBMIT = (By.CSS_SELECTOR, "#button-filter > i")
    SEARCHED_PRODUCT_NAME = (By.XPATH, "//*[@id='form-product']/div/table/tbody/tr/td[3]")
    SEARCHED_PRODUCT_MODEL = (By.XPATH, "//*[@id='form-product']/div/table/tbody/tr/td[4]")
    SEARCHED_PRODUCT_PRICE = (By.XPATH, "//*[@id='form-product']/div/table/tbody/tr/td[5]")
    SEARCHED_PRODUCT_QTY = (By.XPATH, "//*[@id='form-product']/div/table/tbody/tr/td[6]/span")
    FILTER_PANEL = (By.CSS_SELECTOR, "#filter-product > div > div.panel-heading")
    FILTERED_PRODUCT_CHECKBOX = (
        By.CSS_SELECTOR, "#form-product > div > table > tbody > tr > td:nth-child(1) > input[type=checkbox]")
    RESULT_LIST = (By.CSS_SELECTOR, "#form-product > div > table > tbody")
    DELETE_BTN = (By.CSS_SELECTOR, "button[data-original-title='Delete']")
    NO_RESULT_TEXT = (By.CSS_SELECTOR, "#form-product > div > table > tbody > tr > td")

    @property
    def h1_page_title(self):
        return self.get_text(self.H1_TITLE)

    def open_catalog_from_side_menu(self):
        self.click_(self.MENU_CATALOG)

    def open_products_from_catalog(self):
        self.click_(self.CATALOG_PRODUCTS)

    def click_add_product_btn(self):
        self.click_(self.ADD_BTN)

    def click_save_product_btn(self):
        self.click_(self.SAVE_BTN)

    def input_product_name(self, text):
        self.input_(self.PRODUCT_NAME_INPUT, text)

    def input_meta_tag_title(self, text):
        self.input_(self.PRODUCT_METADATA_INPUT, text)

    def switch_tab_to(self, tab: str):
        if tab.strip().upper() == "GENERAL":
            self.click_(self.GENERAL_TAB)
        if tab.strip().upper() == "DATA":
            self.click_(self.DATA_TAB)
        if tab.strip().upper() == "LINKS":
            self.click_(self.LINKS_TAB)
        # else:
        #     raise AssertionError(f"Не смог переключиться на табу {tab}")

    def input_product_model(self, text):
        self.input_(self.PRODUCT_MODEL_INPUT, text)

    def input_product_price(self, text):
        self.input_(self.PRODUCT_PRICE_INPUT, text)

    def input_product_qty(self, text):
        self.input_(self.PRODUCT_QTY_INPUT, text)

    def filter_by_product_name(self, text):
        self.input_(self.FILTER_BY_NAME_INPUT, text)

    def filter_submit_btn(self):
        js_code = "document.querySelector('#button-filter').click();"
        self.driver.execute_script(js_code)

    @property
    def search_result(self):
        result_dict = {
            "name": self.element(self.SEARCHED_PRODUCT_NAME).text,
            "model": self.element(self.SEARCHED_PRODUCT_MODEL).text,
            "price": self.element(self.SEARCHED_PRODUCT_PRICE).text,
            "qty": self.element(self.SEARCHED_PRODUCT_QTY).text
        }
        return result_dict

    def select_filtered_product(self):
        self.click_(self.FILTERED_PRODUCT_CHECKBOX)

    def delete_product(self):
        self.click_(self.DELETE_BTN)
        self.accept_allert()

    def no_results_message_is_present(self):
        return self.element(self.RESULT_LIST).find_element(*self.NO_RESULT_TEXT).text
