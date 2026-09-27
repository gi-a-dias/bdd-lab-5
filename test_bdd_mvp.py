import unittest
from livraria import (
    comprar_retirada,
    verificar_alerta_estoque,
    validar_qr_code,
    BANCO_PEDIDOS
)


class TestBDDMVPLivraria(unittest.TestCase):
    def setUp(self):
        # Limpa o banco de pedidos antes de cada teste
        BANCO_PEDIDOS.clear()

#teste 1 > compra e Retirada
def test_compra_para_retirada(self):
    pedido = comprar_retirada("Gio", "Dom Casmurro")

    # Verifica se o status está correto
    self.assertEqual(pedido["status"], "Pronto para Retirada")

# teste 2 > lerta de Estoque
def test_alerta_estoque_baixo(self):
    notificacao = verificar_alerta_estoque("O Hobbit", 1)
    # Verifica se a mensagem de alerta foi gerada
    self.assertIsNotNone(notificacao)

# teste 3 > validação qrcode
def test_validação_qr_code(self):
    pedido = comprar_retirada("Gio", "Dom Casmurro")
    qrcode = pedido["qrcode"]
    resultado = validar_qr_code(qrcode)

    # Verifica se deu certo a validação
    self.assertEqual(resultado["sucesso"], True)
    self.assertEqual(pedido["status"], "Entregue")

if __name__ == "__main__":
    unittest.main()
