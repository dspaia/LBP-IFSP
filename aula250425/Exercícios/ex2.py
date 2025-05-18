class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_valor_total(self):
        return self.preco * self.quantidade

    def atualizar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade

lista_de_produtos = []
contador = 0

while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade: "))

    produto = Produto(nome, preco, quantidade)
    lista_de_produtos.append(produto)
    contador += 1

    continuar = input("Deseja adicionar outro produto? (s/n): ").lower()
    if continuar == 'n':
        break

print("\nProdutos cadastrados:")
print(f"Total de produtos cadastrados: {contador}")
for produto in lista_de_produtos:
    print(f"Produto: {produto.nome}")
    print(f"Preço: R$ {produto.preco:.2f}")
    print(f"Quantidade: {produto.quantidade}")
    print(f"Valor total: R$ {produto.calcular_valor_total():.2f}")
    

print("\nAtualização de quantidades:")
atualizar = input("Deseja atualizar a quantidade de algum produto? (s/n): ").lower()
if atualizar == 's':
    for produto in lista_de_produtos:
        nova_quantidade = int(input(f"Nova quantidade para {produto.nome} (atual: {produto.quantidade}): "))
        produto.atualizar_quantidade(nova_quantidade)

if atualizar == 's':
    print("\nProdutos após atualização:")
    for produto in lista_de_produtos:
        print(f"{produto.nome} - Quantidade: {produto.quantidade} - Valor total: R$ {produto.calcular_valor_total():.2f}")
else:
    print("\nProdutos:")
    for produto in lista_de_produtos:
        print(f"{produto.nome} - Quantidade: {produto.quantidade} - Valor total: R$ {produto.calcular_valor_total():.2f}")