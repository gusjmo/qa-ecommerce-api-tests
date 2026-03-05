import pytest
import requests

# ==============================================================
# BASE_URL: endereço raiz da API que vamos testar.
# Centralizar aqui significa que se a URL mudar um dia,
# você muda em UM lugar só — não em cada arquivo de teste.
# ==============================================================
BASE_URL = "https://fakestoreapi.com"


@pytest.fixture(scope="session")
def base_url():
    """
    FIXTURE: É uma função especial do Pytest que fornece
    dados ou configurações para os testes.

    scope="session" significa que essa fixture é criada
    UMA VEZ e compartilhada durante toda a execução dos testes.
    Evita criar e destruir o mesmo objeto repetidamente.

    Em entrevista: 'Usei fixtures para centralizar configurações
    e evitar repetição de código nos testes (princípio DRY).'
    """
    return BASE_URL


@pytest.fixture(scope="session")
def session():
    """
    FIXTURE: Cria uma Session do requests.

    requests.Session() reutiliza a mesma conexão HTTP
    para todas as chamadas — mais performático que criar
    uma nova conexão a cada requests.get() individual.

    Em entrevista: 'Usei Session para otimizar a performance
    dos testes, reutilizando conexões HTTP.'
    """
    s = requests.Session()
    yield s
    s.close()  # Fecha a conexão ao final de todos os testes


@pytest.fixture
def produto_payload():
    """
    FIXTURE: Retorna um dicionário com dados de produto.
    Usado nos testes de criação (POST) para não repetir
    os mesmos dados em vários testes.
    """
    return {
        "title": "Produto de Teste QA",
        "price": 99.99,
        "description": "Criado automaticamente via teste",
        "image": "https://fakestoreapi.com/img/81fAn0X5zhL._AC_UY879_.jpg",
        "category": "electronics"
    }
