import pytest
from selenium.webdriver.common.by import By

from PageObject.RegistartionPage import RegistartionPage
from PageObject.AccountSuccessPage import AccountSuccessPage
from faker import *
from tests.ui.utils import *
import allure

fake = Factory.create()
FIRSTNAME_NEW = fake.first_name()
LASTNAME_NEW = fake.last_name()
EMAIL_NEW = fake.email()
PHONE_NEW = fake.phone_number()
PASSWORD = f"password{FIRSTNAME_NEW}"


@pytest.mark.smoke
@allure.epic ("Opencart UI")
@allure.story("Тестовые сценарии")
@allure.title("Регистрация нового пользователя")
def test_register_page(browser):
    """
    Шаги теста:
    1) Зайти на страницу Регистрации
    2) Введем валидные данные нового пользователя в поля:
    -Firstname,
    -Lastname,
    -E-Mail,
    -Telephone,
    -Password,
    -Password Confirm
    3) Подтветдим согласие с Private policy
    4) Завершим регистрацию
    #TODO - проверка создания аккаунта через БД
    """

    with allure.step('1) Зайти на страницу Регистрации'):
        REGISTRATION_PAGE = RegistartionPage(browser)
        REGISTRATION_PAGE.open_(browser.url + REG_PAGE_PATH)
    assert "Register Account" in REGISTRATION_PAGE.h1_title()

    with allure.step('2) Введем валидные данные нового пользователя'):
        REGISTRATION_PAGE.input_firstname(FIRSTNAME_NEW)
        REGISTRATION_PAGE.input_lastname(LASTNAME_NEW)
        REGISTRATION_PAGE.input_email(EMAIL_NEW)
        REGISTRATION_PAGE.input_phone(PHONE_NEW)
        REGISTRATION_PAGE.input_password(PASSWORD)
        REGISTRATION_PAGE.confirm_password(PASSWORD)

    #
    with allure.step('3)Подтветдим согласие с Privat policy'):
        REGISTRATION_PAGE.confirm_private_policy_agreement()

    #
    with allure.step('4)Завершим регистрацию'):
        REGISTRATION_PAGE.confirm_registration()
        assert "Your Account Has Been Created!" in AccountSuccessPage(browser).h1_title()
