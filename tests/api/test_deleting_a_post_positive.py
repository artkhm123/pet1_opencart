import pytest
import requests
import allure

from tests.api.utils import *


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.parametrize("postId", [1, 2, 3])
@allure.epic("jsonplaceholder API")
@allure.story("Простые тесты")
@allure.title(f"Удаление конкретного поста по его id. Позитивные случаи")
def test_deleting_a_post_positive(jsonplaceholder_url, postId):
    """
    Удаление поста. Позитивные кейсы. Метод DELETE
    """
    delete_responce = requests.delete(jsonplaceholder_url + RESOURCES_LIST["posts"] + str(postId))
    assert delete_responce.status_code == 200
    assert delete_responce.json() == {}
