import requests
import pytest

@pytest.mark.smoke
def test_get_all_posts(base_url):
    response = requests.get(f"{base_url}/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0

@pytest.mark.smoke
def test_get_single_post(base_url):
    response = requests.get(f"{base_url}/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert "title" in response.json()
    assert "body" in response.json()

@pytest.mark.regression
@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_multiple_posts(base_url, post_id):
    response = requests.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id

@pytest.mark.regression
def test_create_post(base_url):
    new_post = {
        "title": "AutoQA Test Post",
        "body": "Created by automated test",
        "userId": 1
    }
    response = requests.post(f"{base_url}/posts", json=new_post)
    assert response.status_code == 201
    assert response.json()["title"] == "AutoQA Test Post"

@pytest.mark.regression
def test_invalid_post_returns_404(base_url):
    response = requests.get(f"{base_url}/posts/9999")
    assert response.status_code == 404