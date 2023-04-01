import os

from allure_commons.model2 import Attachment
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import logging
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.default_wait = 2
        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"logs/{self.driver.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.driver.log_level)
        self.wait = WebDriverWait(self.driver, self.default_wait)

    def open_(self, url):
        with allure.step(f"Открыть URL {url}"):
            self.logger.info("Opening url: {}".format(url))
            self.driver.get(url)
            self.logger.info("Opening url: {}".format(url))
            self.driver.get(url)
            try:
                self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))
            except TimeoutException:
                allure.attach(body=self.driver.get_screenshot_as_png(),
                              name="content_not_visible_screenshot")
                raise AssertionError(f"Не дождался видимости контента на странице {url}")

    def browser_back(self):
        with allure.step(f"Навигация в браузере 'Назад'"):
            self.driver.back()

    def click_(self, locator):
        with allure.step(f"Кликнуть по элементу {locator}"):
            self.logger.info("Click on element: {}".format(locator))
            try:
                self.wait.until(EC.element_to_be_clickable(locator)).click()
            except TimeoutException:
                allure.attach(body=self.driver.get_screenshot_as_png(),
                              name="element_not_clicable_screenshot")
                raise AssertionError(f"Не дождался кликабельности поля {locator}")

    def input_(self, field, value):
        with allure.step(f"Вставить текст {value} поле {field}"):
            self.logger.info("Input {} in field {}".format(value, field))
            try:
                find_field = self.wait.until(EC.visibility_of_element_located(field))
                find_field.click()
                find_field.clear()
                find_field.send_keys(value)
            except TimeoutException:
                allure.attach(body=self.driver.get_screenshot_as_png(),
                              name="input_field_not_visible_screenshot")
                raise AssertionError(f"Не дождался видимости поля {field}")

    def accept_allert(self):
        with allure.step("Нажать ОК в браузерной аллерте"):
            self.logger.info("Accept allert on the page".format())
            try:
                alert = self.wait.until(EC.alert_is_present())
                alert.accept()
            except TimeoutException:
                allure.attach(body=self.driver.get_screenshot_as_png(),
                              name="browser_alert_not_present_screenshot")
                raise AssertionError("Не дождался браузерного адерта")

    def element(self, locator: tuple):
        with allure.step(f"Поиск элемента {locator}"):
            self.logger.info("Searching for element {} on the page".format(locator))
            try:
                return self.wait.until(EC.visibility_of_element_located(locator))
            except TimeoutException:
                allure.attach(body=self.driver.get_screenshot_as_png(),
                              name="element_not_visible_screenshot")
                raise AssertionError(f"Не дождался видимости элемента {locator}")

    def elements(self, locator: tuple):
        with allure.step(f"Поиск элементов {locator}"):
            self.logger.info("Searching for elements {} on the page".format(locator))
            try:
                return self.wait.until(EC.visibility_of_all_elements_located(locator))
            except TimeoutException:
                allure.attach(body=self.driver.get_screenshot_as_png(),
                              name="elements_not_visible_screenshot")
                raise AssertionError(f"Не дождался видимости элементов {locator}")

    def get_text(self, locator):
        with allure.step(f"Поиск текста элемента {locator}"):
            self.logger.info("Get text from element {}".format(locator))
            try:
                return self.wait.until(EC.visibility_of_element_located(locator)).text
            except TimeoutException:
                allure.attach(body=self.driver.get_screenshot_as_png(),
                              name="element_not_visible_screenshot")
                raise AssertionError(f"Не дождался видимости заголовка {locator}")
