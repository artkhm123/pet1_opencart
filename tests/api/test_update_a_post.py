import pytest
import requests
import allure

from tests.api.utils import *


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.parametrize("title", ["APPER CASE TITLE", "lower case title", ""])
@pytest.mark.parametrize("body", ["APPER CASE BODY", "lower case body", ""])
@pytest.mark.parametrize("userId", [123, 1])
@pytest.mark.parametrize("postId", [1, 2, 3])
@allure.epic("jsonplaceholder API")
@allure.story("Простые тесты")
@allure.title(f"Апдейт поста")
def test_update_a_post(title, body, userId, postId, jsonplaceholder_url):
    """
    Редактирование поста. Метод PUT
    """
    put_body = {"id": postId, "title": title, "body": body, "userId": userId}
    put_responce = requests.put(jsonplaceholder_url + RESOURCES_LIST["posts"] + str(postId), data=put_body)
    assert put_responce.status_code == 200
    assert put_responce.json()["title"] == title
    assert put_responce.json()["body"] == body
    assert int(put_responce.json()["userId"]) == userId
    assert put_responce.json()["id"] == postId
