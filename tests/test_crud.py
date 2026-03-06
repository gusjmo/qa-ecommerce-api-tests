import requests

BASE_URL = "https://fakestoreapi.com"

NOVO_PRODUTO = {
    "title": "Produto de Teste QA",
    "price": 99.99,
    "description": "Criado via teste automatizado",
    "image": "https://i.pravatar.cc",
    "category": "electronics"
}


def test_criar_produto():
    response = requests.post(f"{BASE_URL}/products", json=NOVO_PRODUTO)

    assert response.status_code in [200, 201], (
        f"Esperado 200 ou 201, recebido {response.status_code}"
    )
    data = response.json()
    assert "id" in data
    assert data["title"] == NOVO_PRODUTO["title"]


def test_atualizar_produto_put():
    produto_atualizado = NOVO_PRODUTO.copy()
    produto_atualizado["title"] = "Produto Atualizado PUT"
    produto_atualizado["price"] = 149.99

    response = requests.put(f"{BASE_URL}/products/1", json=produto_atualizado)

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Produto Atualizado PUT"
    assert float(data["price"]) == 149.99


def test_atualizar_produto_patch():
    atualizacao_parcial = {"price": 199.99}

    response = requests.patch(f"{BASE_URL}/products/1", json=atualizacao_parcial)

    assert response.status_code == 200
    data = response.json()
    assert "id" in data


def test_deletar_produto():
    response = requests.delete(f"{BASE_URL}/products/1")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


def test_listar_produto_deletado():
    # Fake Store API nao persiste dados — DELETE e simulado
    response = requests.get(f"{BASE_URL}/products/1")

    assert response.status_code in [200, 404]
