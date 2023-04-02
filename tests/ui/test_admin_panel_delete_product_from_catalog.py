import pytest
import allure
from PageObject.AdminPanelPage import AdminMainPage
from PageObject.LoginPage import LoginPage
from PageObject.elements.AlertElement import AlertElement
from PageObject.elements.HeaderElement import HeaderElement
from tests.ui.utils import *
import random

TEST_PRODUCT_NAME = f"Test product{random.randint(10, 1000)}"
TEST_PRODUCT_MODEL = f"Test model{random.randint(0, 10)}"
TEST_PRODUCT_PRICE = random.randint(10, 500)
TEST_PRODUCT_QTY = random.randint(1, 500)
TEST_METADATA_TAG = f"Test metadata{random.randint(0, 10)}"


@pytest.mark.smoke
@allure.epic ("Opencart UI")
@allure.story("Тестовые сценарии")
@allure.title('Удаление продукта')
def test_add_and_delete_product(browser):
    """
    Предусловия:
    Пользователь залогинен в админ панель
    Тестовый продукт есть в каталоке

    Шаги теста:
    1) Найти тестовый продукт
    2) Выбрать тестовый продукт
    3) Удалить выбранный продукт
    4) Убедиться, что продукт удален
        -Success Allert
        -Тестового продукта нет в списке продуктов
    #TODO - проверка создания продукта через БД
    """

    with allure.step('Предусловия:' +"\n"
                     'Пользователь залогинен в админ панель' +"\n"
                     'Тестовый продукт есть в каталоке'):
        LOGIN_PAGE = LoginPage(browser)
        LOGIN_PAGE.open_(browser.url + LOGIN_PAGE_PATH)
        LOGIN_PAGE.input_username(OPENCART_USERNAME)
        LOGIN_PAGE.input_password(OPENCART_PASSWORD)
        LOGIN_PAGE.login()
        ADMIN_PAGE = AdminMainPage(browser)
        ADMIN_PAGE.open_catalog_from_side_menu()
        ADMIN_PAGE.open_products_from_catalog()
        ADMIN_PAGE.click_add_product_btn()
        ADMIN_PAGE.input_product_name(TEST_PRODUCT_NAME)
        ADMIN_PAGE.input_meta_tag_title(TEST_METADATA_TAG)
        ADMIN_PAGE.switch_tab_to("Data")
        ADMIN_PAGE.input_product_model(TEST_PRODUCT_MODEL)
        ADMIN_PAGE.click_save_product_btn()

    with allure.step('1) Найти тестовый продукт'):
        ADMIN_PAGE.filter_by_product_name(TEST_PRODUCT_NAME)
        ADMIN_PAGE.filter_submit_btn()

    with allure.step('2) Выбрать тестовый продукт'):
        ADMIN_PAGE.select_filtered_product()

    with allure.step('3) Удалить выбранный продукт'):
        ADMIN_PAGE.delete_product()

    with allure.step('Убедиться, что продукт удален' +"\n"
                     '-Success Allert ' +"\n"
                     '-Тестового продукта нет в списке продуктов'):
        assert "Success: You have modified products!" in AlertElement(browser).success_alert_message_text
        ADMIN_PAGE.filter_by_product_name(TEST_PRODUCT_NAME)
        ADMIN_PAGE.filter_submit_btn()
        assert ADMIN_PAGE.no_results_message_is_present()
