import pytest

from PageObject.RegistartionPage import RegistartionPage
from PageObject.AccountSuccessPage import AccountSuccessPage
from faker import *

from PageObject.elements.AlertElement import AlertElement
from tests.ui.utils import *
import allure

fake = Factory.create()
FIRSTNAME_NEW = fake.first_name()
LASTNAME_NEW = fake.last_name()
EMAIL_NEW = fake.email()
PHONE_NEW = fake.phone_number()
PASSWORD = f"password{FIRSTNAME_NEW}"


@pytest.mark.regress
@allure.epic ("Opencart UI")
@allure.story("Тестовые сценарии")
@allure.title("Проверка обязательности подтверждения Private policy при регистрации нового пользователя")
def test_register_page(browser):
    """
    Шаги теста:
    1) Зайти на страницу Регистрации
    2) Заполнить валидными данными все обязательные поля
    -Firstname,
    -Lastname,
    -E-Mail,
    -Telephone,
    -Password,
    -Password Confirm
    3) Попробовать зарегестрироваться, кликнув по кнопке "Confirm" не подтвердив согласие Privat Policy
    4) Проверить наличия Warning сообщения и неуспешной регистрации
    #TODO - проверка создания аккаунта через БД
    """

    with allure.step('1) Зайти на страницу Регистрации'):
        REGISTRATION_PAGE = RegistartionPage(browser)
        REGISTRATION_PAGE.open_(browser.url + REG_PAGE_PATH)
    assert "Register Account" in REGISTRATION_PAGE.h1_title()

    with allure.step('2) Заполнить валидными данными все обязательные поля'):
        REGISTRATION_PAGE.input_firstname(FIRSTNAME_NEW)
        REGISTRATION_PAGE.input_lastname(LASTNAME_NEW)
        REGISTRATION_PAGE.input_email(EMAIL_NEW)
        REGISTRATION_PAGE.input_phone(PHONE_NEW)
        REGISTRATION_PAGE.input_password(PASSWORD)
        REGISTRATION_PAGE.confirm_password(PASSWORD)

    with allure.step('3)Попробовать зарегестрироваться, кликнув по кнопке "Confirm" не подтвердив согласие Privat Policy'):
        REGISTRATION_PAGE.confirm_registration()

    with allure.step('4) Проверить наличия Warning сообщения и неуспешной регистрации'):
        assert "Warning: You must agree to the Privacy Policy" in AlertElement(browser).warning_alert_message_text
