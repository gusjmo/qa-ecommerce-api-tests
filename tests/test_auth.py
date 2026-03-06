import requests

BASE_URL = "https://fakestoreapi.com"


def test_login_valido():
    payload = {
        "username": "mor_2314",
        "password": "83r5^_"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)

    assert response.status_code in [200, 201], (
        f"Esperado 200 ou 201, recebido {response.status_code}"
    )
    assert "token" in response.json(), "Token nao encontrado na resposta"


def test_login_senha_errada():
    payload = {
        "username": "mor_2314",
        "password": "senha_errada"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)

    assert response.status_code in [400, 401, 403], (
        f"Esperado erro de autenticacao, recebido {response.status_code}"
    )


def test_login_usuario_inexistente():
    payload = {
        "username": "usuario_que_nao_existe",
        "password": "qualquer"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)

    assert response.status_code in [400, 401, 403, 404], (
        f"Esperado erro, recebido {response.status_code}"
    )


def test_login_campos_ausentes():
    payload = {}
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)

    assert response.status_code in [400, 401, 403], (
        f"Esperado erro por campos ausentes, recebido {response.status_code}"
    )
