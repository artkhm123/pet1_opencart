import pytest
import requests
import allure
from jsonschema import validate
from tests.api.utils import *


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.parametrize("resource, schema", [
    (RESOURCES_LIST["posts"], schema_posts),
    (RESOURCES_LIST["comments"], schema_comments),
    (RESOURCES_LIST["albums"], schema_albums),
    (RESOURCES_LIST["photos"], schema_photos),
    (RESOURCES_LIST["todos"], schema_todos),
    (RESOURCES_LIST["users"], schema_users)
])
@allure.epic("jsonplaceholder API")
@allure.story("Простые тесты")
@allure.title(f"Валидация схемы")
def test_jsonplaceholder_schemas_validate(resource, schema, jsonplaceholder_url):
    """Валидация схем для всех ресурсов https://jsonplaceholder.typicode.com:
        posts:      /posts
        comments:   /comments
        albums:     /albums
        photos:     /photos
        todos:      /todos
        users:      /users
    """

    with allure.step(f'Валидация для {resource} '):
        get_response = requests.get(jsonplaceholder_url + resource)
        assert get_response.status_code == 200
        validate(instance=get_response.json(), schema=schema)
