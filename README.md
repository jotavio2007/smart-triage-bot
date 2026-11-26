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
```

## ⚙️ Funcionalidades

- **Classificação de Intenções:** Identifica automaticamente demandas de **Financeiro**, **Suporte Técnico** ou **Dúvida Geral** a partir da mensagem do cliente.
- **Roteamento Inteligente:** Define se o atendimento foi **Resolvido pelo Bot** ou se precisa ser **Encaminhado para Humano**.
- **Persistência em Banco de Dados:** Armazena todas as interações em um banco relacional **SQLite** criado automaticamente na inicialização.
- **Relatório de Métricas (SQL):** Ao encerrar a sessão (`sair`), consolida o total de atendimentos e a distribuição por categoria utilizando consultas agregadas (`COUNT` e `GROUP BY`).

## 🚀 Como Executar Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/jotavio2007/smart-triage-bot.git](https://github.com/jotavio2007/smart-triage-bot.git)
   cd smart-triage-bot
   ```

2. **Execute a aplicação** *(não requer bibliotecas externas além da biblioteca padrão do Python 3)*:
   ```bash
   python main.py
   ```

3. **Interaja com o bot:**
   - Digite o nome do cliente e a mensagem desejada.
   - Digite `sair` no campo de nome para encerrar e visualizar o relatório SQL consolidado.

## 🛠️ Tecnologias Utilizadas

- **Python 3** (Modularização, manipulação de strings, estruturas condicionais e laços)
- **SQLite3** (DDL/DML, prevenção de SQL Injection com queries parametrizadas `?`, `COUNT`, `GROUP BY`)
- **Git & GitHub** (Versionamento semântico e boas práticas com `.gitignore`)

## 📈 Próximos Passos

- [ ] Evoluir o motor de regras (`bot.py`) para classificação semântica via LLM / NLP.
- [ ] Expor o fluxo de triagem e os relatórios em uma API REST e interface web.