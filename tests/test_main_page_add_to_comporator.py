import time

import pytest

from PageObject.MainPage import MainPage
from PageObject.ComparisonPage import ComparisonPage
from PageObject.elements.AlertElement import AlertElement
import allure


@pytest.mark.regress
@allure.epic ("Opencart UI")
@allure.story("Тестовые сценарии")
@allure.title("Главная страница. Добавление продукта в компаратор с продуктовой тумбы")
def test_main_page_elements(browser):
    """
    Предусловия:
    Пользователь на главной странице
    В компараторе нет продуктов

    Шаги теста:
    1) Проверить, что на главной странице 4 продуктовые тумбы
    2) Проверить, что у каждой продуктовой тумбы есть кнопка "Add to Сomporator"
    3) Проверить сообщение при добавлении продукта в компаратор
    4) Проверирть, что продукт появился в компараторе
    """

    with allure.step('Предусловия: Пользоватлель на главной странице'):
        MAIN_PAGE = MainPage(browser)
        MAIN_PAGE.open_(browser.url)

    with allure.step('1) Проверить , что на главной странице 4 продуктовые тумбы'):
        amount_of_tumbs = len(MAIN_PAGE.tumb_list())
        assert amount_of_tumbs == 4

    with allure.step(
            '2) Проверить, что у каждой продуктовой тумбы есть кнопка "Add to Сomporator"'):
        for number in range(amount_of_tumbs):
            assert MAIN_PAGE.add_to_comparison_button_is_present(number)

    for number in range(amount_of_tumbs):
        time.sleep(1)
        with allure.step(f'3) Проверить сообщение при добавлении продукта {number} в компаратор'):
            product_name = MAIN_PAGE.click_compare_this_product(number)
            assert f"Success: You have added {product_name} to your product comparison!" in AlertElement(
                browser).success_alert_message_text
            AlertElement(browser).comparison_allert.click()
            with allure.step(f'4) Проверирть, что продукт {product_name} появился в компараторе'):
                assert ComparisonPage(browser).comparison_product_name(number) == product_name
            time.sleep(1)
            ComparisonPage(browser).browser_back()
