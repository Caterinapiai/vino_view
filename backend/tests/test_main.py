import os
import sys
from fastapi.testclient import TestClient
import json
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
))
from app.main import app

client = TestClient(app)


def test_read_main():
    """
    Test the "/top-wines" endpoint to ensure it
    returns a list of top wines with the expected structure.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the Wine API!",
        "description": ("This API provides information about "
                        "different types of wines.")
    }


def test_get_top_wines():
    """
    Test the endpoint to get top wines by checking the status code,
    the content-type, and the existence of every expected key.
    """
    response = client.get("/top-wines")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    expected_keys = {
        "name",
        "type",
        "country",
        "region",
        "winery",
        "rating",
        "numberofratings",
        "price",
        "year"
    }

    top_wines = json.loads(response.text)

    for wine in top_wines:
        assert set(wine.keys()) == expected_keys


def test_get_most_recent_wines():
    """
    Test the "/most-recent-wines" endpoint to ensure
    it returns a list of most recent wines with the expected structure.
    """
    response = client.get("/most-recent-wines")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    expected_keys = {
        "name",
        "type",
        "country",
        "region",
        "winery",
        "rating",
        "numberofratings",
        "price",
        "year"
    }

    most_recent_wines = json.loads(response.text)

    for wine in most_recent_wines:
        assert set(wine.keys()) == expected_keys


def test_get_countries():
    """
    Test the "/countries" endpoint to ensure
    it returns a list of countries as strings.
    """
    response = client.get("/countries")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    countries = json.loads(response.text)
    assert isinstance(countries, list)
    assert all(isinstance(country, str) for country in countries)


def test_get_types():
    """
    Test the "/types" endpoint to ensure
    it returns a list of wine types as strings.
    """
    response = client.get("/types")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    wine_types = json.loads(response.text)
    assert isinstance(wine_types, list)
    assert all(isinstance(wine_type, str) for wine_type in wine_types)


def test_get_least_recent_wines():
    """
    Test the "/least-recent-wines" endpoint to ensure
    it returns a list of least recent wines with the expected structure.
    """
    response = client.get("/least-recent-wines")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    expected_keys = {
        "name",
        "type",
        "country",
        "region",
        "winery",
        "rating",
        "numberofratings",
        "price",
        "year"
    }

    least_recent_wines = json.loads(response.text)

    for wine in least_recent_wines:
        assert set(wine.keys()) == expected_keys
