import pytest
import allure

from PageObject.CartPage import CartPage
from PageObject.ProductCardPage import ProductCardPage
from PageObject.elements.AlertElement import AlertElement


@pytest.mark.smoke
@pytest.mark.slow
@allure.epic("Opencart UI")
@allure.story("Тестовые сценарии")
@allure.title("Продуктовая страница. Добавление продукта в корзину")
@pytest.mark.parametrize("product", ["/iphone", "/macbook"])
def test_product_card_page(browser, product):
    """
    Предусловия:
    Пользователь на продуктовой странице
    В корзине нет продуктов "Найдем значение которое отображается "в корзине" перед началом теста"

    Шаги теста:
    1) Найти цену товара
    2) Найти количество товара
    3) Кликнуть по кнопке Add to cart
    4) Проверить сообщение при добавлении продукта в корзину
    5) Проверить, что значение в каунтере изменилось.
    6) Проверить, что продукт появился в корзине

    Постусловия: удалить добавленный продукт
    """
    # stop("#fb-root");

    PRODUCT_CARD_PAGE = ProductCardPage(browser)

    with allure.step(f'Предусловия: Пользователь на {product} странице'):
        PRODUCT_CARD_PAGE.open_(browser.url + product)
        cart_counter_before = PRODUCT_CARD_PAGE.cart_counter()
        product_name = PRODUCT_CARD_PAGE.product_name()

    with allure.step('1) Найти цену товара'):
        product_price_float = float(PRODUCT_CARD_PAGE.get_product_price().replace('$', ''))

    with allure.step('2) Найти количество товара'):
        product_qty = PRODUCT_CARD_PAGE.product_qty()

    with allure.step('3) Кликнуть по кнопке Add to cart'):
        PRODUCT_CARD_PAGE.add_to_cart_btn_click()

    with allure.step('4) Проверить сообщение при добавлении продукта в корзину'):
        assert f"Success: You have added {product_name} to your shopping cart!" in AlertElement(
            browser).success_alert_message_text

    with allure.step('5) Проверить, что значение в каунтере изменилось на корректное'):
        cart_counter_after = PRODUCT_CARD_PAGE.cart_counter()
        assert cart_counter_before != cart_counter_after
        assert cart_counter_after == f"{str(product_qty)} item(s) - ${str(format(product_qty * product_price_float, '.2f'))}"

    with allure.step('6) Проверить, что продукт появился в корзине'):
        AlertElement(browser).shoping_cart_allert.click()
        assert CartPage(browser).product_in_cart_name() == product_name
        assert CartPage(browser).product_in_cart_qty() == product_qty
        assert CartPage(browser).product_in_cart_price() == product_price_float

    with allure.step('Постусловия: удалить добавленный продукт'):
        CartPage(browser).remove_product()
