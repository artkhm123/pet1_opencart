import time

import pytest

from PageObject.MainPage import MainPage
from PageObject.elements.AlertElement import AlertElement
import allure


@pytest.mark.regress
@allure.epic("Opencart UI")
@allure.story("Тестовые сценарии")
@allure.title("Главная страница. Нельзя добавить продукт с продуктовой тумбы в вишлист не залогинившись")
def test_main_page_elements(browser):
    """
    Предусловия:
    Пользователь на главной странице
    Пользователь не залогинен

    Шаги теста:
    1) Проверить, что на главной странице 4 продуктовые тумбы
    2) Проверить, что у каждой продуктовой тумбы есть кнопка "Add to wishlist"
    3) Проверить сообщение при добавлении продукта в wishlist для незалогиненного пользователя
    """

    with allure.step('Предусловия: Пользоватлель на главной странице'):
        MAIN_PAGE = MainPage(browser)
        MAIN_PAGE.open_(browser.url)

    with allure.step('1)проверка что продуктовых тумбы 4шт'):
        amount_of_tumbs = len(MAIN_PAGE.tumb_list())
        assert amount_of_tumbs == 4

    with allure.step(
            '2)Проверить, что у каждой продуктовой тумбы есть кнопка "Add to wishlist"'):
        for number in range(amount_of_tumbs):
            assert MAIN_PAGE.add_to_wish_list_button_is_present(number)

    for number in range(amount_of_tumbs):
        time.sleep(1)
        with allure.step(
                f'3) Проверить сообщение при добавлении продукта {number} в вишлист не залогиненным рользователем'):
            product_name = MAIN_PAGE.click_add_to_wishlist(number)
            assert f"You must login or create an account to save {product_name} to your wish list!" in AlertElement(
                browser).success_alert_message_text
