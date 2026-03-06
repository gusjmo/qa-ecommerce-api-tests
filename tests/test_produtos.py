import pytest
import requests

BASE_URL = "https://fakestoreapi.com"


@pytest.mark.parametrize("produto_id", [1, 2, 3, 4, 5])
def test_buscar_produto_por_id(produto_id):
    response = requests.get(f"{BASE_URL}/products/{produto_id}")

    assert response.status_code == 200, (
        f"Produto {produto_id} retornou {response.status_code}"
    )
    data = response.json()
    assert data["id"] == produto_id
    assert "title" in data
    assert "price" in data
    assert "category" in data


def test_listar_todos_produtos():
    response = requests.get(f"{BASE_URL}/products")

    assert response.status_code == 200
    produtos = response.json()
    assert isinstance(produtos, list)
    assert len(produtos) > 0


def test_listar_produtos_com_limite():
    response = requests.get(f"{BASE_URL}/products?limit=5")

    assert response.status_code == 200
    produtos = response.json()
    assert len(produtos) == 5


@pytest.mark.parametrize("categoria", [
    "electronics",
    "jewelery",
    "men's clothing",
    "women's clothing"
])
def test_listar_por_categoria(categoria):
    response = requests.get(f"{BASE_URL}/products/category/{categoria}")

    assert response.status_code == 200
    produtos = response.json()
    assert isinstance(produtos, list)
    assert len(produtos) > 0
    for produto in produtos:
        assert produto["category"] == categoria


def test_produto_inexistente():
    response = requests.get(f"{BASE_URL}/products/99999")

    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json() is None or response.json() == {}
