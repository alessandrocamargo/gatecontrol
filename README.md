
# 🚪 Sistema de Controle de Portaria (GateControl)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red)
![Status](https://img.shields.io/badge/status-MVP%20funcional-green)
![License](https://img.shields.io/badge/license-MIT-green)

Sistema web desenvolvido para gerenciamento operacional de portarias
empresariais, com foco no **controle de veículos internos**, registro de
movimentações e rastreabilidade operacional em tempo real.

---

## 📌 Sobre o Projeto

O Sistema de Controle de Portaria foi criado para resolver problemas
reais encontrados em empresas que utilizam controle manual de veículos:

- ❌ registros inconsistentes
- ❌ ausência de histórico confiável
- ❌ dificuldade de auditoria
- ❌ controle manual de quilometragem

O sistema digitaliza todo o processo operacional, garantindo controle,
segurança e histórico centralizado.

---

## 🎯 Objetivo

Criar uma aplicação web corporativa capaz de:

- Gerenciar veículos internos por setor
- Registrar saída e retorno de veículos
- Controlar quilometragem automaticamente
- Permitir operação rápida pela portaria
- Aplicar regras operacionais reais
- Fornecer visão operacional via dashboard

---

## 🧱 Arquitetura

Frontend (HTML / Bootstrap / JS)
        ↓
Flask Blueprints (Routes / Controllers)
        ↓
Regras de Negócio
        ↓
SQLAlchemy Models (ORM)
        ↓
Database (SQLite/PostgreSQL)

---

## ⚙️ Tecnologias Utilizadas

### Backend
- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- Flask-Migrate

### Frontend
- HTML5
- Bootstrap 5
- JavaScript (Fetch API)
- Jinja2 Templates

### Banco de Dados
- SQLite (desenvolvimento)
- PostgreSQL (planejado para produção)

---

## 🔐 Controle de Acesso

| Perfil | Permissões |
|------|------------|
| admin | Administração completa |
| operador | Registrar saída e retorno |
| cadastro | Cadastro de dados base |

---

## 📊 Dashboard Operacional

- Total de veículos
- Veículos disponíveis
- Veículos em uso
- Ações rápidas diretamente na tabela

---

## 🚗 Movimentação de Veículos

### Saída
- Informar KM inicial
- Horário automático
- Status → Em uso

### Retorno
- Informar KM final
- Validação automática
- Status → Disponível

---

## ✅ Regras de Negócio

- Veículo não pode ter duas saídas abertas
- Retorno exige saída ativa
- KM final > KM inicial
- Horários automáticos

---

## 🚀 Como Executar

```bash
git clone https://github.com/alessandrocamargo/gatecontrol.git
cd gatecontrol
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
flask db upgrade
flask run
```

Acesse:

http://127.0.0.1:5000

---

## 📈 Roadmap

### Próximo
- Registro de visitantes
- Registro de prestadores

### Futuro
- Relatórios
- API REST
- Mobile
- Leitura automática de placas

---

## 👨‍💻 Autor

**Alessandro André Sanches Gonzaga de Camargo**  
GitHub: https://github.com/alessandrocamargo
