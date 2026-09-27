\# language:pt
Funcionalidade: MVP do Aplicativo da Livraria Física e Digital
Cenário: Realizar compra para retirada na loja física com QR Code
Dado que o cliente "Gio" escolheu o livro "Dom Casmurro"
Quando ele finaliza a compra para retirar na loja
Então o sistema deve gerar um pedido com status "Pronto para Retirada"

Cenário: Enviar alerta quando o estoque atingir 1 unidade
Dado que o livro "O Hobbit" está no estoque
Quando o estoque cai para 1 unidade
Então o sistema deve gerar um alerta de estoque crítico

Cenário: Conferência do QR Code na entrega do pedido
Dado que o pedido tem o status "Pronto para Retirada"
Quando a equipe lê o QR Code do pedido
Então o status do pedido deve mudar para "Entregue"