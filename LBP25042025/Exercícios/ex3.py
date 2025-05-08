class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_valor_total(self):
        return self.preco * self.quantidade


class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto):
        self.itens.append(produto)

    def remover_produto(self, nome_produto):
        self.itens = [produto for produto in self.itens if produto.nome.lower() != nome_produto.lower()]

    def calcular_total(self):
        return sum(produto.calcular_valor_total() for produto in self.itens)

    def listar_itens(self):
        if not self.itens:
            print("Carrinho vazio.")
        else:
            for produto in self.itens:
                print(f"{produto.nome} - Quantidade: {produto.quantidade} - Preço: R$ {produto.preco:.2f} - Total: R$ {produto.calcular_valor_total():.2f}")
            print(f"\nValor total do carrinho: R$ {self.calcular_total():.2f}")


carrinho = CarrinhoDeCompras()

while True:
    print("\n--- Menu Carrinho de Compras ---")
    print("[1] Adicionar produto")
    print("[2] Remover produto")
    print("[3] Ver carrinho")
    print("[0] Encerrar programa")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade: "))
        produto = Produto(nome, preco, quantidade)
        carrinho.adicionar_produto(produto)
        print("Produto adicionado com sucesso!")

    elif escolha == '2':
        nome_para_remover = input("Digite o nome do produto que deseja remover: ")
        carrinho.remover_produto(nome_para_remover)
        print("Se o produto existia, foi removido.")

    elif escolha == '3':
        print("\n--- Itens no carrinho ---")
        carrinho.listar_itens()

    elif escolha == '0':
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
