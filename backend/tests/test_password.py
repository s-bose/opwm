from .client import client, temp_db


test_entries = [
    {
        "site": "Google",
        "link": "www.google.com",
        "username": "hello",
        "password": "world"
    },
    {
        "site": "Youtube",
        "link": "www.youtube.com",
        "username": "hello2",
        "password": "world2"
    }
]

@temp_db
def test_insert_one():
    res = client.post("/api/passwords/", json=test_entries[0])
    res = client.post("/api/passwords/", json=test_entries[1])
    
    assert res.status_code == 200


@temp_db
def test_get():
    response = client.get("/api/passwords/all")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2


