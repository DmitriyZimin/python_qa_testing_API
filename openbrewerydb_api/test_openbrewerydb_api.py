import pytest
import requests


def test_list_breweries(openbrewerydb_api_base_url):
    response = requests.get(openbrewerydb_api_base_url)

    assert response.status_code == 200, "Статус код ответа = 200"
    assert response.reason == 'OK', "Статус ответа = OK"


def test_random_brewery(openbrewerydb_api_base_url):
    response = requests.get(openbrewerydb_api_base_url + "/random")

    assert response.status_code == 200, "Статус код ответа = 200"
    assert response.reason == 'OK', "Статус ответа = OK"


@pytest.mark.parametrize("page_number", [1, 3, 10])
def test_brewery_per_page(page_number, openbrewerydb_api_base_url):
    response = requests.get(openbrewerydb_api_base_url + f"?per_page={page_number}")

    assert response.status_code == 200, "Статус код ответа = 200"
    assert response.reason == 'OK', "Статус ответа = OK"
    assert len(response.json()) == page_number


@pytest.mark.parametrize("state", ["Colorado", "California", "Arizona"])
def test_brewery_by_state(state, openbrewerydb_api_base_url):
    state_lower_case = state.lower()

    response = requests.get(openbrewerydb_api_base_url + f"?by_state={state_lower_case}")
    brewery_state_list = list(map(lambda x: x.get('state'), response.json()))

    assert response.status_code == 200, "Статус код ответа = 200"
    assert response.reason == 'OK', "Статус ответа = OK"
    assert brewery_state_list
    assert all(state == item for item in brewery_state_list)


@pytest.mark.parametrize("brewery_type", ["brewpub", "large", "bar"])
def test_brewery_by_state(brewery_type, openbrewerydb_api_base_url):
    response = requests.get(openbrewerydb_api_base_url + f"?by_type={brewery_type}")
    brewery_type_list = list(map(lambda x: x.get('brewery_type'), response.json()))

    assert response.status_code == 200, "Статус код ответа = 200"
    assert response.reason == 'OK', "Статус ответа = OK"
    assert brewery_type_list
    assert all(brewery_type == item for item in brewery_type_list)
