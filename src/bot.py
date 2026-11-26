def classificar_intencao(mensagem):
    texto = mensagem.lower()

    if "boleto" in texto or "pagar" in texto or "fatura" in texto:
        return "Financeiro", "Resolvido pelo Bot"
    elif "suporte" in texto or "erro" in texto or "não funciona" in texto:
        return "Suporte Técnico", "Encaminhado para Humano"
    elif "cancelar" in texto or "encerrar" in texto:
        return "Cancelamento", "Encaminhado para Retenção"
    else:
        return "Dúvida Geral", "Resolvido pelo Bot"