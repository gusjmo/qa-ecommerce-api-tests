# ==============================================================
# test_crud.py — Testes de operações CRUD
#
# CRUD = Create, Read, Update, Delete
# São as 4 operações básicas de qualquer sistema.
# Cada uma mapeada para um método HTTP:
#   Create  -> POST
#   Read    -> GET
#   Update  -> PUT / PATCH
#   Delete  -> DELETE
# ==============================================================

import requests

BASE_URL = "https://fakestoreapi.com"


def test_criar_produto():
    """
    Testa a criação de um novo produto via POST.

    requests.post(url, json=payload):
      - url: o endpoint que recebe a criação
      - json=payload: converte automaticamente o dicionário
        Python para JSON e define o header Content-Type correto

    Status 200 ou 201:
      - 200 = OK genérico
      - 201 = Created (mais correto semanticamente)
      A Fake Store retorna 200, mas em APIs reais espera-se 201.

    Em entrevista: 'Entendo a diferença entre 200 e 201:
    200 é sucesso genérico, 201 significa que um recurso
    foi criado com sucesso no servidor.'
    """
    payload = {
        "title": "Produto de Teste QA",
        "price": 99.99,
        "description": "Criado automaticamente via teste automatizado",
        "image": "https://fakestoreapi.com/img/81fAn0X5zhL._AC_UY879_.jpg",
        "category": "electronics"
    }

    response = requests.post(f"{BASE_URL}/products", json=payload)

    assert response.status_code in [200, 201], (
        f"Esperado 200 ou 201, recebido {response.status_code}"
    )

    produto_criado = response.json()
    assert "id" in produto_criado, "Produto criado deveria ter um ID"
    assert produto_criado["title"] == payload["title"]
    assert produto_criado["price"] == payload["price"]


def test_atualizar_produto():
    """
    Testa atualização completa de produto via PUT.

    PUT: substitui o recurso COMPLETO.
    PATCH: atualiza apenas os campos enviados (parcial).

    Em entrevista: 'Sei a diferença entre PUT e PATCH:
    PUT substitui o objeto inteiro, PATCH só os campos enviados.'
    """
    payload_atualizado = {
        "title": "Produto Atualizado",
        "price": 149.99,
        "description": "Descrição atualizada via teste",
        "image": "https://fakestoreapi.com/img/81fAn0X5zhL._AC_UY879_.jpg",
        "category": "electronics"
    }

    response = requests.put(
        f"{BASE_URL}/products/1",
        json=payload_atualizado
    )

    assert response.status_code == 200
    produto = response.json()
    assert produto["title"] == payload_atualizado["title"]


def test_atualizar_parcialmente_produto():
    """
    Testa atualização parcial via PATCH.
    Enviamos apenas o campo que queremos alterar.
    """
    payload_parcial = {"price": 59.99}

    response = requests.patch(
        f"{BASE_URL}/products/1",
        json=payload_parcial
    )

    assert response.status_code == 200


def test_deletar_produto():
    """
    Testa exclusão de produto via DELETE.

    Importante: a Fake Store API simula a exclusão mas
    não remove o produto de verdade (API de teste).
    Em APIs reais, após DELETE bem-sucedido um GET
    no mesmo ID deveria retornar 404.

    Em entrevista: 'Após testar DELETE, sempre valido
    que o recurso realmente não existe mais com um GET.'
    """
    response = requests.delete(f"{BASE_URL}/products/1")

    assert response.status_code == 200, (
        f"DELETE deveria retornar 200, recebido {response.status_code}"
    )

    produto_deletado = response.json()
    assert produto_deletado["id"] == 1
