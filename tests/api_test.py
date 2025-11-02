import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"


@pytest.mark.parametrize(
    "id, username, firstName, lastName, email, password, phone, userStatus",
    [
        (1111, 'Ring-bearer', 'Frodo', 'Baggins',
         'frodo@shire.com', 'test', '555111', 0),
        (1112, 'Hobbit', 'Bilbo', 'Baggins',
         'bilbo@shire.com', 'test', '555111', 0),
    ],
)
def test_create_user(id, username, firstName, lastName, email, password, phone, userStatus):
    # locals() возвращает все локальные переменные функции
    # payload = {k: v for k, v in locals().items()}
    payload = {
        "id": id,
        "username": username,
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "password": password,
        "phone": phone,
        "userStatus": userStatus
    }
    url = f"{BASE_URL}/user"
    response = requests.post(url, json=payload)

    # Check response status code
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    # Check response body keys
    data = response.json()
    assert set(data.keys()) == {"code", "type", "message"}, "Response keys do not match"

    # Check headers
    assert "Content-Type" in response.headers, "Content-Type header is missing"
    assert response.headers["Content-Type"] == "application/json", "Content-Type value is incorrect"

    assert "Access-Control-Allow-Methods" in response.headers, "Access-Control-Allow-Methods header is missing"
    assert response.headers["Access-Control-Allow-Methods"].replace(" ", "") == "GET,POST,DELETE,PUT", \
        "Access-Control-Allow-Methods value is incorrect"