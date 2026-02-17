# 🚪 Sistema de Controle de Portaria

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

Sistema web desenvolvido para gerenciamento operacional de portarias
empresariais, com foco no **controle de veículos internos**, registro de
entradas e saídas e rastreabilidade operacional.

------------------------------------------------------------------------

## 📌 Sobre o Projeto

O Sistema de Controle de Portaria foi criado para resolver problemas
reais encontrados em empresas que utilizam controle manual de veículos:

-   ❌ registros inconsistentes
-   ❌ ausência de histórico confiável
-   ❌ dificuldade de auditoria
-   ❌ controle manual de quilometragem

O sistema digitaliza todo o processo, garantindo controle e histórico
centralizado.

------------------------------------------------------------------------

## 🎯 Objetivo

Criar uma aplicação web corporativa capaz de:

-   Registrar pessoas
-   Gerenciar veículos internos por setor
-   Controlar saída e entrada de veículos
-   Registrar quilometragem automaticamente
-   Garantir regras operacionais reais

------------------------------------------------------------------------

## 🧱 Arquitetura

O projeto segue arquitetura em camadas baseada no padrão MVC adaptado ao
Flask:

    Frontend (HTML/CSS/JS)
            ↓
    Flask Routes / Controllers
            ↓
    Business Rules
            ↓
    SQLAlchemy Models
            ↓
    Database (SQLite/PostgreSQL)

------------------------------------------------------------------------

## ⚙️ Tecnologias Utilizadas

### Backend

-   Python
-   Flask
-   Flask-SQLAlchemy
-   Flask-Migrate

### Frontend

-   HTML5
-   CSS3
-   JavaScript
-   Jinja2 Templates

### Banco de Dados

-   SQLite (desenvolvimento)
-   PostgreSQL (planejado para produção)

------------------------------------------------------------------------

## 📂 Estrutura do Projeto

    app/
    │
    ├── models/
    │   ├── usuario.py
    │   ├── pessoa.py
    │   ├── setor.py
    │   ├── veiculo.py
    │   └── movimentacao_veiculo.py
    │
    ├── routes/
    │   ├── auth.py
    │   ├── pessoas.py
    │   ├── veiculos.py
    │   └── movimentacoes.py
    │
    ├── templates/
    ├── static/
    │
    ├── extensions.py
    └── __init__.py

------------------------------------------------------------------------

## 🚗 Funcionalidade Principal --- Movimentação de Veículos

### Saída

-   Operador seleciona veículo
-   Informa quilometragem
-   Sistema registra horário automaticamente
-   Veículo muda para **Em uso**

### Entrada

-   Operador registra retorno
-   Informa quilometragem final
-   Sistema calcula percurso
-   Veículo volta para **Disponível**

------------------------------------------------------------------------

## ✅ Regras de Negócio

-   Um veículo não pode sair duas vezes simultaneamente
-   Entrada só ocorre se houver saída aberta
-   KM de entrada deve ser maior que KM de saída
-   Horários são registrados automaticamente

------------------------------------------------------------------------

## 🔐 Segurança

-   Senhas armazenadas com hash
-   Controle de acesso por perfil
-   Rotas protegidas por autenticação
-   Preparado para Flask-Login

------------------------------------------------------------------------

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar repositório

``` bash
git clone https://github.com/seu-usuario/sistema-portaria.git
cd sistema-portaria
```

### 2️⃣ Criar ambiente virtual

``` bash
python -m venv venv
venv\Scripts\activate
```

(Linux/Mac)

``` bash
source venv/bin/activate
```

### 3️⃣ Instalar dependências

``` bash
pip install -r requirements.txt
```

### 4️⃣ Configurar banco

``` bash
flask db upgrade
```

### 5️⃣ Executar aplicação

``` bash
flask run
```

Acesse:

    http://127.0.0.1:5000

------------------------------------------------------------------------

## 📈 Roadmap

### Curto Prazo

-   Dashboard operacional
-   Relatórios por veículo

### Médio Prazo

-   API REST
-   Autenticação JWT

### Longo Prazo

-   Aplicativo Mobile (React Native)
-   Leitura automática de placas
-   Deploy em cloud

------------------------------------------------------------------------

## 🧠 Decisões Técnicas

-   **Flask** escolhido pela flexibilidade arquitetural
-   **SQLAlchemy ORM** para abstração do banco
-   **Blueprints** para modularização
-   **Flask-Migrate** para versionamento seguro do banco

------------------------------------------------------------------------

## ⭐ Diferenciais

Este projeto não é apenas um CRUD:

✅ Modelagem baseada em operação real\
✅ Controle de estado do veículo\
✅ Regras corporativas implementadas\
✅ Estrutura escalável

------------------------------------------------------------------------

## 👨‍💻 Autor

**Alessandro André Sanches Gonzaga de Camargo**\
Desenvolvedor Web Fullstack (em formação)

🔗 GitHub: https://github.com/sancamargosan

------------------------------------------------------------------------

## 📄 Documentação Completa

Consulte também a documentação técnica completa em PDF incluída no
repositório: `documentacao_sistema_portaria.pdf`
