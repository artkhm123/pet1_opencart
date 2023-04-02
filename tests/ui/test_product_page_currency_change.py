import pytest
from PageObject.elements.HeaderElement import HeaderElement
from PageObject.ProductCardPage import ProductCardPage
import allure

from tests.ui.utils import *


@pytest.mark.slow
@pytest.mark.regress
@allure.epic("Opencart UI")
@allure.story("Тестовые сценарии")
@allure.title("Смена валюты на странице 'карточка продукта'")
@pytest.mark.parametrize("product, prices", [("/iphone", IPHONE_PRICE), ("/macbook", MAC_PRICE)])
def test_currency_change(browser, product, prices):
    """
    Предусловия:
       Пользователь на продуктовой странице

    Шаги теста:
    1) Сменить валюту на USD
    2) Проверить что цена в USD корректна
    3) Сменить валюту на EUR
    4) Проверить что цена в EUR корректна
    5) Сменить валюту на GBP
    6) Проверить что цена в GBP корректна
    """
    # stop("#fb-root");

    price_dict = prices
    PRODUCT_CARD_PAGE = ProductCardPage(browser)

    with allure.step(f'Предусловия: Пользователь на {product} странице'):
        PRODUCT_CARD_PAGE.open_(browser.url + product)

    with allure.step('1) сменить валюту на USD'):
        HeaderElement(browser).change_currency_to("USD")

    with allure.step('2) проверить что цена в USD корректна'):
        assert PRODUCT_CARD_PAGE.get_product_price() == price_dict["USD"]

    with allure.step('3) сменить валюту на EUR'):
        HeaderElement(browser).change_currency_to("EUR")

    with allure.step('4) проверить что цена в EUR корректна'):
        assert PRODUCT_CARD_PAGE.get_product_price() == price_dict["EUR"]

    with allure.step('5) сменить валюту на GBP'):
        HeaderElement(browser).change_currency_to("GBP")

    with allure.step('6) проверить что цена в GBP корректна'):
        assert PRODUCT_CARD_PAGE.get_product_price() == price_dict["GBP"]
