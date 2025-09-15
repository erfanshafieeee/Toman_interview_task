import pytest
import requests
import json
from jsonschema import validate, ValidationError


response_schema = {
    "type": "object",
    "properties": {
        "status": {"type": "integer"},
        "data": {
            "type": "object",
            "properties": {
                "data_layer": {
                    "type": "object",
                    "properties": {
                        "event": {"type": "string"},
                        "ecommerce": {"type": "object"}
                    }
                },
                "cart_items": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "cart_id": {"type": "integer"},
                            "quantity": {"type": "integer"},
                            "price": {
                                "type": "object",
                                "properties": {
                                    "price": {"type": "integer"},
                                    "discount": {"type": "integer"}
                                }
                            },
                            "product": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "integer"},
                                    "title_fa": {"type": "string"},
                                    "url": {"type": "object"}
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "required": ["status", "data"]
}


BASE_URL = "https://api.digikala.com/v2/cart/add/"

product_data = {
    "variant_ids": [70672040],
    "pass": True
}


def make_api_request(data):
    try:
        response = requests.post(BASE_URL, json=data)
        response.raise_for_status()  # to raise HTTPError for bad responses
        return response
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")
        return None  # return None in case of failure


@pytest.mark.parametrize("data", [product_data])
def test_api_status_code(data):
    response = make_api_request(data)
    assert response is not None, "API request failed"
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


@pytest.mark.parametrize("data", [product_data])
def test_api_schema(data):
    response = make_api_request(data)
    assert response is not None, "API request failed"
    try:
        validate(instance=response.json(), schema=response_schema)
    except ValidationError as e:
        pytest.fail(f"Schema validation error: {e.message}")


if __name__ == "__main__":
    pytest.main()
