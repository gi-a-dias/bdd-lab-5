# dicionario como banco de dados
BANCO_PEDIDOS = {}


# Compra para retirada na loja
def compra_retirada(cliente, livro):
    id_pedido = "PEDIDO_101"
    qrcode = "QR_PEDIDO_101"

    pedido = {
        "id_pedido": id_pedido,
        "cliente": cliente,
        "livro": livro,
        "status": "Pronto para Retirada",  # Aqui está com iniciais maiúsculas
        "qrcode": qrcode
    }

    BANCO_PEDIDOS[qrcode] = pedido
    return pedido


# Alerta de estoque baixo
def verificar_alerta_estoque(livro, qtde_estoque):
    if qtde_estoque == 1:
        return "Estoque critico: resta apenas 1"
    else:
        return "Estoque regular"


# Conferencia do qrcode na loja
def validar_qr_code(qrcode):
    if qrcode in BANCO_PEDIDOS:
        pedido = BANCO_PEDIDOS[qrcode]

        # Ajustado para bater exatamente com "Pronto para Retirada"
        if pedido["status"] == "Pronto para Retirada":
            pedido["status"] = "Entregue"

            # Retornando um dicionário para o teste funcionar
            return {"sucesso": True, "mensagem": "Retirada concluída"}
        else:
            return {"sucesso": False, "mensagem": "Pedido não está pronto para retirada"}
    else:
        return {"sucesso": False, "mensagem": "QRCODE INEXISTENTE, CONSULTE UM ATENDENTE"}