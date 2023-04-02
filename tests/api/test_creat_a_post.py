import pytest
import requests
import allure

from tests.api.utils import *


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.parametrize("title", ["APPER CASE TITLE", "lower case title", ""])
@pytest.mark.parametrize("body", ["APPER CASE BODY", "lower case body", ""])
@pytest.mark.parametrize("userId", [123, 1])
@allure.epic("jsonplaceholder API")
@allure.story("Простые тесты")
@allure.title(f"Создание поста")
def test_creat_a_post(title, body, userId, jsonplaceholder_url):
    """
    Создание поста. Метод POST
    """
    post_body = {"title": title, "body": body, "userId": userId}
    post_responce = requests.post(jsonplaceholder_url + RESOURCES_LIST["posts"], data=post_body)
    assert post_responce.status_code == 201
    assert post_responce.json()["title"] == title
    assert post_responce.json()["body"] == body
    assert int(post_responce.json()["userId"]) == userId
    assert post_responce.json()["id"] == 101
