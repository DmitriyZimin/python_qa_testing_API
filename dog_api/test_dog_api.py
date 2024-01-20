import json
import re

import pytest
import requests


def test_list_all_breeds(dog_api_base_url):
    response = requests.get(dog_api_base_url + "/breeds/list/all")
    assert response.status_code == 200, "Статус код ответа = 200"
    assert response.reason == 'OK', "Статус ответа = OK"


def test_random_breed_image(dog_api_base_url):
    response = requests.get(dog_api_base_url + "/breeds/image/random")
    assert response.status_code == 200, "Статус код ответа = 200"
    assert response.reason == 'OK', "Статус ответа = OK"


@pytest.mark.parametrize("breed", ["Akita", "Sharpei", "Eskimo"])
def test_breeds_list(breed, dog_api_base_url):
    response = requests.get(dog_api_base_url + f"/breed/{breed.lower()}/images/random")
    data = response.json()

    assert response.status_code == 200, "Статус код ответа = 200"
    assert response.reason == 'OK', "Статус ответа = OK"
    assert re.findall(f".*/{breed.lower()}/.*\\.jpg", data['message'])


@pytest.mark.parametrize("breed", ["Australian", "Bulldog", "Corgi"])
def test_sub_breed_list(breed, dog_api_base_url):
    breed_lower_case = breed.lower()

    response_breeds = requests.get(dog_api_base_url + "/breeds/list/all")
    response_breeds_dict = json.loads(response_breeds.text)
    breeds = response_breeds_dict['message']

    response_sub_breeds = requests.get(dog_api_base_url + f"/breed/{breed_lower_case}/list")
    response_sub_breeds_dict = json.loads(response_sub_breeds.text)
    sub_breeds = response_sub_breeds_dict['message']

    assert response_sub_breeds.status_code == 200, "Статус код ответа = 200"
    assert response_sub_breeds.reason == 'OK', "Статус ответа = OK"
    assert breeds[breed_lower_case] == sub_breeds


@pytest.mark.parametrize("image_number", [1, 3])
@pytest.mark.parametrize("breed", ["Terrier", "Spaniel", "Retriever"])
def test_sub_breed_multiple_images(image_number, breed, dog_api_base_url):
    breed_lower_case = breed.lower()

    response_sub_breeds = requests.get(dog_api_base_url + f"/breed/{breed_lower_case}/images/random/{image_number}")

    assert response_sub_breeds.status_code == 200, "Статус код ответа = 200"
    assert response_sub_breeds.reason == 'OK', "Статус ответа = OK"
