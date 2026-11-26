from src.database import criar_tabela, salvar_conversa, gerar_relatorio
from src.bot import classificar_intencao

def iniciar_bot():
    criar_tabela()
    print("=== Smart Triage Bot Iniciado (digite 'sair' para encerrar) ===")

    while True:
        cliente = input("\nNome do cliente: ")
        if cliente.lower() == "sair":
            break

        mensagem = input("Mensagem: ")
        intencao, status = classificar_intencao(mensagem)
        salvar_conversa(cliente, mensagem, intencao, status)

        print(f"-> Triagem: [{intencao}] | Status: {status}")

    total, por_intencao = gerar_relatorio()
    print(f"\n=== Relatório Final: {total} atendimentos ===")
    for item, qtd in por_intencao:
        print(f"- {item}: {qtd}")

if __name__ == "__main__":
    iniciar_bot()