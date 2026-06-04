import requests
import pytest

def test_get_all_users(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_single_user(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert "name" in response.json()
    assert "email" in response.json()

@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_multiple_users(base_url, user_id):
    response = requests.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id

def test_invalid_user_returns_404(base_url):
    response = requests.get(f"{base_url}/users/9999")
    assert response.status_code == 404

def test_response_time(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.elapsed.total_seconds() < 3