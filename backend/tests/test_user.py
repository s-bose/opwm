from .client import client, temp_db

@temp_db
def test_user_register():
    response = client.post("/api/register", json={"email": "abc@abc.com", "master_pwd": "pass"})
    assert response.status_code == 200

@temp_db
def test_user_login():
    response = client.post("/api/login", json={"email": "abc@abc.com", "master_pwd": "pass"})
    assert response.status_code == 200

@temp_db
def test_get_user():
   
    response = client.get("/api/user")
    assert response.status_code == 200
    assert response.json().get("email") == "john@doe.com"