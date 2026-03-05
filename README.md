# 🛒 QA — Testes Automatizados de API E-commerce

<div align="center">

[![Testes de API](https://github.com/gusjmo/qa-ecommerce-api-tests/actions/workflows/testes.yml/badge.svg)](https://github.com/gusjmo/qa-ecommerce-api-tests/actions/workflows/testes.yml)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2CA5E0?style=for-the-badge&logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

![Status](https://img.shields.io/badge/Status-Ativo-brightgreen?style=flat-square)
![Testes](https://img.shields.io/badge/Testes-15%2B%20casos-blue?style=flat-square)
![Tipo](https://img.shields.io/badge/Tipo-Portf%C3%B3lio%20QA-purple?style=flat-square)

</div>

---

## 📖 Sobre o Projeto

Suite de testes automatizados de **API REST** que simula um fluxo real de e-commerce, cobrindo autenticação, operações CRUD, validação de schema e regras de negócio.

Desenvolvido com foco em demonstrar habilidades práticas de **Quality Assurance** utilizando ferramentas e padrões do mercado.

**API testada:** [Fake Store API](https://fakestoreapi.com) — API REST pública que simula um e-commerce completo.

---

## 🧪 Cobertura de Testes

### 🔐 Autenticação (`test_auth.py`)
| Cenário | Tipo | Descrição |
|---------|------|-----------|
| Login válido | ✅ Positivo | Credenciais corretas retornam token |
| Login senha errada | ❌ Negativo | Senha incorreta não deve autenticar |
| Usuário inexistente | ❌ Negativo | Usuário inválido não deve autenticar |
| Validação JWT | 🔍 Estrutural | Token retornado é um JWT válido (3 partes) |

### 📦 Produtos (`test_produtos.py`)
| Cenário | Tipo | Descrição |
|---------|------|-----------|
| Listar todos | ✅ Positivo | Endpoint retorna lista não vazia |
| Schema de produto | 🔍 Estrutural | Valida campos obrigatórios em todos os produtos |
| Busca por ID (x5) | ✅ Parametrizado | IDs 1, 2, 3, 10 e 20 com `@parametrize` |
| Filtro por categoria (x4) | ✅ Parametrizado | 4 categorias validando dados retornados |
| Preço maior que zero | 📋 Regra de negócio | Nenhum produto pode ter preço inválido |

### ⚙️ CRUD (`test_crud.py`)
| Cenário | Método | Descrição |
|---------|--------|-----------|
| Criar produto | POST | Criação com validação de ID e dados |
| Atualizar produto | PUT | Substituição completa do recurso |
| Atualizar parcialmente | PATCH | Atualização de campo único |
| Deletar produto | DELETE | Exclusão com validação da resposta |

---

## 🛠️ Tecnologias e Conceitos Aplicados

| Tecnologia / Conceito | Finalidade |
|----------------------|------------|
| **Python 3.11** | Linguagem principal |
| **Pytest** | Framework de testes — execução, fixtures e relatórios |
| **Requests** | Biblioteca HTTP para chamadas à API REST |
| **pytest-html** | Geração de relatório visual em HTML |
| **GitHub Actions** | CI/CD — executa testes a cada push automaticamente |
| **Fixtures** | Configurações reutilizáveis entre testes (`conftest.py`) |
| **@parametrize** | Múltiplos cenários em uma única função de teste |
| **Schema validation** | Validação da estrutura do JSON retornado |
| **Business rules** | Validação de regras de negócio além do status code |

---

## 📁 Estrutura do Projeto

```
qa-ecommerce-api-tests/
├── tests/
│   ├── conftest.py          # Fixtures compartilhadas (base_url, session, payload)
│   ├── test_auth.py         # Testes de autenticação e JWT
│   ├── test_produtos.py     # Listagem, busca, schema e regras de negócio
│   └── test_crud.py         # POST, GET, PUT, PATCH, DELETE
├── .github/
│   └── workflows/
│       └── testes.yml       # Pipeline CI/CD com geração de relatório HTML
├── requirements.txt         # Dependências do projeto
└── README.md
```

---

## 🚀 Como Executar Localmente

### Pré-requisitos
- Python 3.11+
- pip

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/gusjmo/qa-ecommerce-api-tests.git
cd qa-ecommerce-api-tests

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute todos os testes
pytest tests/ -v

# 4. Execute com relatório HTML
pytest tests/ -v --html=relatorio.html --self-contained-html
```

### Exemplo de saída

```
tests/test_auth.py::test_login_valido PASSED
tests/test_auth.py::test_login_senha_errada PASSED
tests/test_auth.py::test_login_usuario_inexistente PASSED
tests/test_auth.py::test_login_retorna_token_jwt PASSED
tests/test_produtos.py::test_listar_todos_produtos PASSED
tests/test_produtos.py::test_estrutura_do_produto PASSED
tests/test_produtos.py::test_buscar_produto_por_id_valido[1] PASSED
tests/test_produtos.py::test_buscar_produto_por_id_valido[2] PASSED
...
15 passed in 3.42s
```

---

## ⚙️ CI/CD com GitHub Actions

A cada `push` ou `pull request` na branch `main`, o GitHub executa automaticamente:

1. Instala o Python e as dependências
2. Roda todos os testes com Pytest
3. Gera um relatório HTML com os resultados
4. Disponibiliza o relatório como artefato para download na aba **Actions**

---

## 📚 Conceitos de QA Demonstrados

- **Happy path**: validação do fluxo esperado e correto
- **Negative testing**: validação de cenários de erro e falha
- **Schema testing**: verificação da estrutura do contrato de API
- **Business rule testing**: validação de regras de negócio além do status HTTP
- **DRY principle**: uso de fixtures e parametrize para evitar repetição
- **CI/CD**: integração contínua com execução automática de testes

---

## 👨‍💻 Autor

**Gustavo Juvencio** — [@gusjmo](https://github.com/gusjmo)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gustavo-juvencio/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/gusjmo)

---

<div align="center">
  <sub>Projeto de portfólio — QA & Automação de Testes de API | 2026</sub>
</div>
