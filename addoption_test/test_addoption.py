import requests


def test_listing_all_resources(ya_url, ya_status_code):
    response = requests.get(ya_url)

    assert response.status_code == ya_status_code
