import pytest

from PageObject.LoginPage import LoginPage
from tests.ui.utils import *
import allure


@pytest.mark.regress
@allure.epic("Opencart UI")
@allure.story("Тестовые сценарии")
@allure.title("Не успешный логин в админ панель")
def test_incorrect_login(browser):
    """
    Шаги теста:
    1) Зайти на страницу логина в админ панель
    2) Ввести не верный username
    3) Ввести не верный password
    4) Проверить, что блок о не верных данных "No match for Username and/or Password" - отсутствует
    5) Нажать кнопку login
    6) Проверить, что блок о не верных данных "No match for Username and/or Password" - появился
    """

    with allure.step('1) Зайти на страницу логина в админ панель'):
        LOGIN_PAGE = LoginPage(browser)
        LOGIN_PAGE.open_(browser.url + LOGIN_PAGE_PATH)
        assert "Please enter your login details." in LOGIN_PAGE.h1_page_title()

    with allure.step('2) Ввести не валидный username'):
        LOGIN_PAGE.input_username(NON_EXISTING_USERNAME)

    with allure.step('3) Ввести не валидный password'):
        LOGIN_PAGE.input_password(WRONG_PASSWORD)

    with allure.step('4) Проверить, что блок о не верных данных "No match for Username and/or Password" - отсутствует'):
        assert not LOGIN_PAGE.wrong_userdata_message_is_present()

    with allure.step('5) Нажать кнопку login'):
        LOGIN_PAGE.login()

    with allure.step('6) Проверить, что блок о не верных данных "No match for Username and/or Password" - появился'):
        assert LOGIN_PAGE.wrong_userdata_message_is_present()
        assert "No match for Username and/or Password." in LOGIN_PAGE.wrong_userdata_message()
