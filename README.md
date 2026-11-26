# 🤖 Smart Triage Bot

Sistema de triagem inteligente de atendimento via terminal desenvolvido em **Python** e **SQLite**, projetado com arquitetura modular para classificar intenções de clientes, persistir históricos de conversa e gerar relatórios analíticos de desempenho.

## 🎯 Objetivo do Projeto

Simular o fluxo real de um motor de atendimento automatizado (estilo plataformas de mensageria e chatbots corporativos), separando a camada de regras de negócio da camada de persistência de dados e oferecendo métricas imediatas ao final de cada sessão.

## 🏗️ Arquitetura do Projeto

O código segue o princípio de **Separação de Responsabilidades** (*Separation of Concerns*):

```text
smart-triage-bot/
├── main.py            # Orquestrador da aplicação (interface CLI e fluxo de execução)
├── src/
│   ├── bot.py         # Motor de triagem e classificação de intenções/status
│   └── database.py    # Camada de persistência SQLite e consultas analíticas (SQL)
├── .gitignore         # Ignora arquivos temporários e bancos locais (*.db)
└── README.md          # Documentação do projeto