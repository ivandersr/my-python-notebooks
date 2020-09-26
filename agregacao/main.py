from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

produto1 = Produto('Mouse', 20)
produto2 = Produto('Teclado', 40)
produto3 = Produto('Pasta térmica', 2.50)

carrinho.inserir_produto(produto1)
carrinho.inserir_produto(produto2)
carrinho.inserir_produto(produto1)

carrinho.lista_produtos()
print(carrinho.soma_total())

# Mouse 20
# Teclado 40
# Mouse 20
# 80
