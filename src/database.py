import sqlite3

def conectar():
    conn = sqlite3.connect("data/triagem.db")
    return conn

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            mensagem TEXT NOT NULL,
            intencao TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def salvar_conversa(cliente, mensagem, intencao, status):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO conversas (cliente, mensagem, intencao, status) VALUES (?, ?, ?, ?)",
        (cliente, mensagem, intencao, status)
    )
    conn.commit()
    conn.close()

def gerar_relatorio():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM conversas")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT intencao, COUNT(*) FROM conversas GROUP BY intencao")
    por_intencao = cursor.fetchall()

    conn.close()
    return total, por_intencao