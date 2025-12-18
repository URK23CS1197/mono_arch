from app import app
import os

def test_file_write():
    client = app.test_client()

    response = client.post("/", data={
        "title": "Test Book",
        "author": "Test Author",
        "price": "100"
    })

    assert response.status_code == 302  # redirect

    with open("data.txt", "r") as f:
        content = f.read()

    assert "Test Book" in content
