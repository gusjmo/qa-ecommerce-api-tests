# ==============================================================
# test_auth.py — Testes de autenticação
#
# Testar login é FUNDAMENTAL em qualquer sistema real.
# Todo QA precisa saber validar: credencial correta,
# credencial errada e campos ausentes.
# ==============================================================

import requests

BASE_URL = "https://fakestoreapi.com"


def test_login_valido():
    """
    Testa login com credenciais válidas.

    requests.post(): envia dados para o servidor via método POST.
    POST é usado quando queremos ENVIAR dados (login, cadastro, etc.)
    ao contrário do GET que apenas busca informações.

    response.status_code: número que indica o resultado da requisição.
      200 = OK (sucesso)
      401 = Não autorizado
      404 = Não encontrado
      500 = Erro interno do servidor

    response.json(): converte a resposta da API (texto JSON)
    em um dicionário Python que conseguimos manipular.
    """
    payload = {
        "username": "mor_2314",
        "password": "83r5^_"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)

    assert response.status_code in [200, 201], (
    f"Esperado 200 ou 201, recebido {response.status_code}"
)

    dados = response.json()

    # Valida que o token foi retornado na resposta
    assert "token" in dados, "Token não encontrado na resposta"
    assert len(dados["token"]) > 0, "Token retornado está vazio"


def test_login_senha_errada():
    """
    Testa login com senha incorreta.
    A API deve retornar erro (status diferente de 200).

    Em QA, testar cenários negativos é tão importante
    quanto testar o caminho feliz (happy path).
    """
    payload = {
        "username": "mor_2314",
        "password": "senha_errada_123"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)

    # A API retorna 401 para credenciais inválidas
    assert response.status_code != 200, (
        "Login com senha errada não deveria retornar 200"
    )


def test_login_usuario_inexistente():
    """
    Testa login com usuário que não existe no sistema.
    Outro cenário negativo importante.
    """
    payload = {
        "username": "usuario_que_nao_existe",
        "password": "qualquer_senha"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)

    assert response.status_code != 200, (
        "Login com usuário inexistente não deveria ter sucesso"
    )


def test_login_retorna_token_jwt():
    """
    Valida que o token retornado é um JWT válido.

    JWT (JSON Web Token) é o padrão de autenticação
    mais usado em APIs modernas. Ele é composto por
    3 partes separadas por ponto: header.payload.signature

    Em entrevista: 'Validei não só o status code, mas também
    a estrutura do token JWT retornado pela API.'
    """
    payload = {
        "username": "mor_2314",
        "password": "83r5^_"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)
    token = response.json().get("token", "")

    # JWT tem exatamente 3 partes separadas por ponto
    partes = token.split(".")
    assert len(partes) == 3, (
        f"Token não parece ser um JWT válido. Partes: {len(partes)}"
    )
