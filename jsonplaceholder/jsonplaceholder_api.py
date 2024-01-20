import pytest
import requests


def test_listing_all_resources(jsonplaceholder_api_base_url):
    response = requests.get(jsonplaceholder_api_base_url)

    assert response.status_code == 200, "Статус код ответа = 200"
    assert response.reason == 'OK', "Статус ответа = OK"


def test_creating_resource(jsonplaceholder_api_base_url):
    jsonobject = {
        "title": 'Test',
        "body": 'test file',
        "userId": '123'
    }

    response = requests.post(jsonplaceholder_api_base_url, json=jsonobject)

    assert response.status_code == 201, "Статус код ответа = 201"
    assert response.reason == 'Created', "Статус ответа = Created"
    assert response.json()["title"] == jsonobject["title"]
    assert response.json()["body"] == jsonobject["body"]
    assert response.json()["userId"] == jsonobject["userId"]
    assert response.json()["id"] == 101


@pytest.mark.parametrize("id_", [1, 2, 3])
@pytest.mark.parametrize("user_id", [10, 20, 30])
def test_updating_resource(id_, user_id, jsonplaceholder_api_base_url):
    jsonobject = {
        "id": id_,
        "title": 'Test_update',
        "body": 'test file update',
        "userId": user_id
    }

    response = requests.put(jsonplaceholder_api_base_url + f"/{id_}", json=jsonobject)

    assert response.status_code == 200, "Статус код ответа = 200"
    assert response.reason == 'OK', "Статус ответа = OK"
    assert response.json()["title"] == jsonobject["title"]
    assert response.json()["body"] == jsonobject["body"]
    assert response.json()["userId"] == jsonobject["userId"]
    assert response.json()["id"] == id_


@pytest.mark.parametrize("id_", [1, 2, 3])
def test_patching_resource(id_, jsonplaceholder_api_base_url):
    jsonobject = {
        "title": 'Test_patch'
    }

    response = requests.patch(jsonplaceholder_api_base_url + f"/{id_}", json=jsonobject)

    assert response.status_code == 200, "Статус код ответа = 200"
    assert response.reason == 'OK', "Статус ответа = OK"
    assert response.json()["title"] == jsonobject["title"]
    assert response.json()["id"] == id_


@pytest.mark.parametrize("id_", [1, 2, 3])
def test_deleting_resource(id_, jsonplaceholder_api_base_url):
    response = requests.delete(jsonplaceholder_api_base_url + f"/{id_}")

    assert response.status_code == 200, "Статус код ответа = 200"
    assert response.reason == 'OK', "Статус ответа = OK"
