import pytest
import requests
import allure

from tests.api.utils import *


@pytest.mark.xfail
@pytest.mark.regress
@pytest.mark.api
@pytest.mark.parametrize("postId", [-11, 0, 200, "str"],
                         ids=["negative = -11",
                              "zero = 0",
                              "over the border = 200",
                              "string = str"])
@allure.epic("jsonplaceholder API")
@allure.story("Простые тесты")
@allure.title(f"Удаление конкретного поста по его id. Негативные случаи")
def test_deleting_a_post_negative(jsonplaceholder_url, postId):
    """
    Удаление поста. Негативные кейсы. Метод DELETE
    """
    delete_responce = requests.delete(jsonplaceholder_url + RESOURCES_LIST["posts"] + str(postId))
    assert delete_responce.status_code == 404
    assert delete_responce.json() == {}
