#dicionario como banco de dados
BANCO_PEDIDOS = {}
#Compra para retirada na loja
def comprar_retirada(cliente, livro):
    id_pedido = "PEDIDO_101"
    qrcode = "QR_PEDIDO_101"

    #montando lista de dados do pedido
    pedido = {
        "id_pedido": id_pedido,
        "cliente": cliente,
        "livro": livro,
        "status": status,
        "qrcode": qrcode
    }

    #salvando o pedido
    BANCO_PEDIDOS[qrcode] = pedido
    return pedido

#Alerta de estoque baixo

def verificar_alerta_estoque(livro, qtde_estoque):
    #estoque = 1
    if qtde_estoque ==1:
        mensagem = "Estoque critico: resta apenas 1"
        return mensagem
    else:
        mensagem = "Estoque regular"
        return mensagem

#Conferencia do qrcode na loja

def validar_qr_code(qrcode):
    #verifica se o qrcode esta no banco
    if qrcode in BANCO_PEDIDOS:
        pedido = BANCO_PEDIDOS[qrcode]

        #mudanca de status: pronto para retirar > entregue
        if pedido["status"] == "pronto para retirar":
            pedido["status"] = "entregue"

            return "Retirada concluída"
        else:
            return "Pedido não esta pronto para retirada"

    else:
        #qrcode nao existe
        return "QRCODE INEXISTENTE, CONSULTE UM ATENDENTE"
