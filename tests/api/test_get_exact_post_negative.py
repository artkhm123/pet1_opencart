import pytest
import requests
import allure

from tests.api.utils import *


@pytest.mark.regress
@pytest.mark.api
@pytest.mark.parametrize("post_number", [-1, 0, 101, "str"],
                         ids=["negative = -1",
                              "zero = 0",
                              "over the border = 101",
                              "string = str"])
@allure.epic("jsonplaceholder API")
@allure.story("Простые тесты")
@allure.title(f"Получение конкретного поста по его id. Негативные случаи")
def test_get_exact_post_negative(post_number, jsonplaceholder_url):
    """
    Получение конкретного поста по его id
    Негативные случаи: id за пределами доступного или строка
    """
    get_response = requests.get(jsonplaceholder_url + RESOURCES_LIST["posts"] + str(post_number))
    assert get_response.status_code == 404
    assert get_response.json() == {}
