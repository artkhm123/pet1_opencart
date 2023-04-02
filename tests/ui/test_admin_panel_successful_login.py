import pytest

from PageObject.AdminPanelPage import AdminMainPage
from PageObject.LoginPage import LoginPage
from PageObject.elements.HeaderElement import HeaderElement
from tests.ui.utils import *
import allure


@pytest.mark.smoke
@allure.epic("Opencart UI")
@allure.story("Тестовые сценарии")
@allure.title("Успешный логин в админ панель")
def test_incorrect_login(browser):
    """
    Шаги теста:
    1) Зайти на страницу логина в админ панель
    2) Ввести верный username
    3) Ввести верный password
    4) Нажать кнопку login
    5) Проверить, что мы вошли в админ панель
    """

    with allure.step('1) Зайти на страницу логина в админ панель'):
        LOGIN_PAGE = LoginPage(browser)
        LOGIN_PAGE.open_(browser.url + LOGIN_PAGE_PATH)
        assert "Please enter your login details." in LOGIN_PAGE.h1_page_title()

    with allure.step('2) Ввести валидный username'):
        LOGIN_PAGE.input_username(OPENCART_USERNAME)

    with allure.step('3) Ввести валидный password'):
        LOGIN_PAGE.input_password(OPENCART_PASSWORD)

    with allure.step('4) Нажать кнопку login'):
        LOGIN_PAGE.login()

    with allure.step('5) Проверить, что мы вошли в админ панель'):
        assert HeaderElement(browser).user_name == "John Doe"
        ADMIN_PAGE = AdminMainPage(browser)
        assert "Dashboard" in ADMIN_PAGE.h1_page_title
