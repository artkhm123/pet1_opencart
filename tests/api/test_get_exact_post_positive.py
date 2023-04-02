import pytest
import requests
import allure

from tests.api.utils import *


@pytest.mark.regress
@pytest.mark.api
@allure.epic("jsonplaceholder API")
@allure.story("Простые тесты")
@allure.title(f"Получение конкретного поста по его id. Позитивные случаи")
def test_get_exact_post_positive(jsonplaceholder_url):
    """
    Получение конкретного поста по его id
    Позитивные случаи: id = randon int [1,100]
    """
    with allure.step(f'Получение конкретного поста по его id'):
        post_num = random.randint(1, POSTS_AMAUNT)
        get_response = requests.get(jsonplaceholder_url + RESOURCES_LIST["posts"] + str(post_num))
        assert get_response.status_code == 200
        assert get_response.json()["id"] == post_num
