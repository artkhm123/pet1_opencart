from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage


class CatalogPage(BasePage):
    CONTENT = (By.CSS_SELECTOR, "#content")
    BREADCRUMBS = (By.CSS_SELECTOR, ".breadcrumb > li")
    H2_TITLE = (By.CSS_SELECTOR, "h2")
    SIDE_BAR = (By.CSS_SELECTOR, "#column-left")
    MAC_SUBCATEGORY = (By.CSS_SELECTOR, f"#column-left > div > a[href='http://192.168.31.28:8081/desktops/mac']")
    PRODUCT_TUMB = (By.CSS_SELECTOR, ".product-thumb")
    IMG = (By.TAG_NAME, "img")

    def navigate_to_Desktops_through_side_bar(self):
        aside_block = self.element(self.SIDE_BAR)
        aside_block.find_element(By.PARTIAL_LINK_TEXT, "Desktops").click()

    def h1_page_title(self):
        return self.get_text(self.H2_TITLE)

    def first_breadcrumb_text(self):
        return self.elements(self.BREADCRUMBS)[1].text

    def select_subcategory_Mac(self):
        self.click_(self.MAC_SUBCATEGORY)

    def second_breadcrumb_text(self):
        return self.elements(self.BREADCRUMBS)[2].text

    def first_product_img_alt(self):
        first_product = self.elements(self.PRODUCT_TUMB)[0]
        return (first_product.find_element(*self.IMG)).get_attribute("alt")
