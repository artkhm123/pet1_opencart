import pytest
import allure
from PageObject.AdminPanelPage import AdminMainPage
from PageObject.LoginPage import LoginPage
from PageObject.elements.AlertElement import AlertElement
from PageObject.elements.HeaderElement import HeaderElement
from utils import *
import random

TEST_PRODUCT_NAME = f"Artem Test product{random.randint(10, 1000)}"
TEST_PRODUCT_MODEL = f"Test model{random.randint(0, 10)}"
TEST_PRODUCT_PRICE = random.randint(10, 500)
TEST_PRODUCT_QTY = random.randint(1, 500)
TEST_METADATA_TAG = f"Test metadata{random.randint(0, 10)}"


@pytest.mark.smoke
@allure.epic ("Opencart UI")
@allure.story("Тестовые сценарии")
@allure.title('Добавление продукта')
def test_add_and_delete_product(browser):
    """
    Предусловия:
    Пользователь залогинен в админ панель

    Шаги теста:
    1) Выбрать в боковом меню Catalog
    2) В выпавшем списке выбрать Products
    3) Нажать Add New
    4) На табе General -> заполнить обязательные поля:
        Product Name
        Meta Tag Title
    5) На табе Data -> заполнить поля:
        Model
        Quantity
        Price
    8) Нажать кнопку "Сохранить"
    9) Проверить, что продукт сохранился:
    -Success Allert
    -Найти созданный продукт в списке продуктов
    #TODO - проверка создания продукта через БД

    Постусловия:
     - Удалить созданный продукт
    """

    with allure.step('Предусловия: Пользователь залогинен в админ панель'):
        LOGIN_PAGE = LoginPage(browser)
        LOGIN_PAGE.open_(browser.url + LOGIN_PAGE_PATH)
        LOGIN_PAGE.input_username(OPENCART_USERNAME)
        LOGIN_PAGE.input_password(OPENCART_PASSWORD)
        LOGIN_PAGE.login()
        assert HeaderElement(browser).user_name == "John Doe"

    with allure.step('1) Выбрать в боковом меню Catalog'):
        ADMIN_PAGE = AdminMainPage(browser)
        ADMIN_PAGE.open_catalog_from_side_menu()

    with allure.step('2) В выпавшем списке выбрать Products'):
        ADMIN_PAGE.open_products_from_catalog()

    with allure.step('3) Нажать Add New'):
        ADMIN_PAGE.click_add_product_btn()

    with allure.step('4) На табе General -> заполнить обязательные поля:/'
                     '   - Product Name/'
                     '   - Meta Tag Title'):
        ADMIN_PAGE.input_product_name(TEST_PRODUCT_NAME)
        ADMIN_PAGE.input_meta_tag_title(TEST_METADATA_TAG)

    with allure.step('6) На табе Data -> заполнить поля:'):
        ADMIN_PAGE.switch_tab_to("Data")
        with allure.step('Model'):
            ADMIN_PAGE.input_product_model(TEST_PRODUCT_MODEL)
        with allure.step('Quantity'):
            ADMIN_PAGE.input_product_price(TEST_PRODUCT_PRICE)
        with allure.step('Price'):
            ADMIN_PAGE.input_product_qty(TEST_PRODUCT_QTY)

    with allure.step('7) Нажать кнопку "Сохранить"'):
        ADMIN_PAGE.click_save_product_btn()

    with allure.step('8) Проверить, что продукт сохранился: /'
                     '   - Success Allert /'
                     '   - Найти созданный продукт в списке продуктов /'
                     '   - Проверить цену, количество и модель'):
        assert "Success: You have modified products!" in AlertElement(browser).success_alert_message_text
        ADMIN_PAGE.filter_by_product_name(TEST_PRODUCT_NAME)
        ADMIN_PAGE.filter_submit_btn()
        assert ADMIN_PAGE.search_result["name"] == TEST_PRODUCT_NAME
        assert ADMIN_PAGE.search_result["model"] == TEST_PRODUCT_MODEL
        assert float(ADMIN_PAGE.search_result["price"].replace('$', '')) == float(TEST_PRODUCT_PRICE)
        assert int(ADMIN_PAGE.search_result["qty"]) == TEST_PRODUCT_QTY

    with allure.step('Постусловия: Удалить созданный продукт'):
        ADMIN_PAGE.filter_by_product_name(TEST_PRODUCT_NAME)
        ADMIN_PAGE.filter_submit_btn()
        ADMIN_PAGE.select_filtered_product()
        ADMIN_PAGE.delete_product()
