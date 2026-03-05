# ==============================================================
# test_produtos.py — Testes de listagem e busca de produtos
#
# Aqui usamos pytest.mark.parametrize, que é uma das
# ferramentas mais importantes e valorizadas em QA.
# ==============================================================

import pytest
import requests

BASE_URL = "https://fakestoreapi.com"


def test_listar_todos_produtos():
    """
    Valida que o endpoint de listagem retorna com sucesso
    e que a resposta é uma lista não vazia.

    isinstance(dados, list): verifica se o objeto é do tipo lista.
    Em Python, tudo tem um tipo. Verificar o tipo da resposta
    é boa prática pois garante que a API não mudou seu contrato.
    """
    response = requests.get(f"{BASE_URL}/products")

    assert response.status_code == 200
    dados = response.json()
    assert isinstance(dados, list), "Resposta deveria ser uma lista"
    assert len(dados) > 0, "Lista de produtos não deveria estar vazia"


def test_estrutura_do_produto():
    """
    Valida que cada produto tem os campos obrigatórios esperados.

    Este é um teste de 'schema' ou 'contrato de API':
    garantimos que a estrutura dos dados não mudou.
    Em empresas reais isso evita que o front-end quebre
    quando o back-end muda sem avisar.
    """
    response = requests.get(f"{BASE_URL}/products")
    produtos = response.json()
    campos_obrigatorios = ["id", "title", "price", "category", "image"]

    for produto in produtos:
        for campo in campos_obrigatorios:
            assert campo in produto, (
                f"Campo '{campo}' ausente no produto id={produto.get('id')}"
            )


@pytest.mark.parametrize("produto_id", [1, 2, 3, 10, 20])
def test_buscar_produto_por_id_valido(produto_id):
    """
    Testa busca por IDs válidos usando parametrize.

    @pytest.mark.parametrize: executa o MESMO teste várias vezes
    com valores diferentes. Aqui testamos 5 IDs diferentes
    sem duplicar nenhuma linha de código.

    Sem parametrize, precisaríamos de 5 funções idênticas.
    Com parametrize, temos 1 função e 5 casos de teste.

    Em entrevista: 'Usei parametrize para aumentar a cobertura
    de testes seguindo o princípio DRY.'
    """
    response = requests.get(f"{BASE_URL}/products/{produto_id}")

    assert response.status_code == 200, (
        f"Produto id={produto_id} deveria existir"
    )
    produto = response.json()
    assert produto["id"] == produto_id


@pytest.mark.parametrize("categoria", [
    "electronics",
    "jewelery",
    "men's clothing",
    "women's clothing"
])
def test_filtrar_por_categoria(categoria):
    """
    Testa filtro por categoria com todas as categorias da API.

    Valida que:
    1. O endpoint retorna 200
    2. A lista não está vazia
    3. Todos os itens pertencem à categoria solicitada

    O ponto 3 é o mais importante: não basta retornar 200,
    temos que garantir que os DADOS estão corretos.
    """
    response = requests.get(
        f"{BASE_URL}/products/category/{categoria}"
    )

    assert response.status_code == 200
    produtos = response.json()
    assert len(produtos) > 0, f"Categoria '{categoria}' veio vazia"

    for produto in produtos:
        assert produto["category"] == categoria, (
            f"Produto fora da categoria! Esperado: '{categoria}', "
            f"Recebido: '{produto['category']}'"
        )


def test_preco_produto_maior_que_zero():
    """
    Valida regra de negócio: preço sempre deve ser positivo.

    Testar REGRAS DE NEGÓCIO é o que diferencia um bom QA.
    Não basta a API retornar 200 — os dados precisam fazer sentido.
    """
    response = requests.get(f"{BASE_URL}/products")
    produtos = response.json()

    for produto in produtos:
        assert produto["price"] > 0, (
            f"Preço inválido no produto id={produto['id']}: {produto['price']}"
        )
