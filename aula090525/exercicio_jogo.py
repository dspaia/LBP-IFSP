#PARTE 1 - MODELANDO O JOGO

class Jogo:
    def __init__(self, titulo, genero, classificacao_etaria, preco):
        self.titulo = titulo
        self.genero = genero
        self.classificacao_etaria = classificacao_etaria
        self.preco = preco

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Gênero: {self.genero}")
        print(f"Classificação Etária: {self.classificacao_etaria}")
        print(f"Preço: R$ {self.preco:.2f}")
        print("-" * 30)

#PARTE 2 - MODELANDO O JOGADOR

class Jogador:
    def __init__(self, nickname, id_jogador, saldo_inicial=0.0):
        self.nickname = nickname
        self.id_jogador = id_jogador
        self.biblioteca_de_jogos = []
        self.saldo_carteira = saldo_inicial

    def exibir_perfil(self):
        print("\n=== Perfil do Jogador ===")
        print(f"Nickname: {self.nickname}")
        print(f"ID do Jogador: {self.id_jogador}")
        print(f"Saldo: R$ {self.saldo_carteira:.2f}")
        print("Jogos na Biblioteca:")
        if self.biblioteca_de_jogos:
            for jogo in self.biblioteca_de_jogos:
                print(f"- {jogo.titulo}")
        else:
            print("Nenhum jogo comprado ainda.")
        print("=" * 30)

    def adicionar_jogo_biblioteca(self, jogo_comprado):
        self.biblioteca_de_jogos.append(jogo_comprado)

    def adicionar_saldo(self, valor):
        self.saldo_carteira += valor

    def debitar_saldo(self, valor):
        if self.saldo_carteira >= valor:
            self.saldo_carteira -= valor
            return True
        return False
    
#PARTE 3 - MODELANDO A PLATAFORMA DE JOGOS

class PlataformaDeJogos:
    def __init__(self, nome_plataforma):
        self.nome_plataforma = nome_plataforma
        self.catalogo_de_jogos = []
        self.jogadores_cadastrados = []

    def adicionar_jogo_catalogo(self, jogo):
        self.catalogo_de_jogos.append(jogo)

    def adicionar_jogador(self, jogador):
        self.jogadores_cadastrados.append(jogador)

    def buscar_jogo_por_titulo(self, titulo_jogo):
        for jogo in self.catalogo_de_jogos:
            if jogo.titulo.lower() == titulo_jogo.lower():
                return jogo
        return None

    def buscar_jogador_por_id(self, id_jogador):
        for jogador in self.jogadores_cadastrados:
            if jogador.id_jogador == id_jogador:
                return jogador
        return None

    def listar_jogos_catalogo(self):
        print(f"\n--- Catálogo de Jogos - {self.nome_plataforma} ---")
        for idx, jogo in enumerate(self.catalogo_de_jogos, start=1):
            print(f"[{idx}]")
            jogo.exibir_detalhes()

    def realizar_compra(self, jogador, jogo):
        if jogo in jogador.biblioteca_de_jogos:
            print("Você já possui este jogo.")
            return

        if jogador.debitar_saldo(jogo.preco):
            jogador.adicionar_jogo_biblioteca(jogo)
            print("Compra realizada com sucesso!")
        else:
            print("Saldo insuficiente para realizar a compra.")

#PARTE 4 - TESTES E SIMULAÇÕES

plataforma = PlataformaDeJogos("GAMEPASS")

plataforma.adicionar_jogo_catalogo(Jogo("Minecraft", "SandBox", "Livre", 74.95))
plataforma.adicionar_jogo_catalogo(Jogo("Far Cry 4", "Ação", "18+", 74.95))
plataforma.adicionar_jogo_catalogo(Jogo("Duna", "Sobravivência", "Livre", 39.90))
plataforma.adicionar_jogo_catalogo(Jogo("Call of Duty: Warzone", "FPS", "18+", 0.99))
plataforma.adicionar_jogo_catalogo(Jogo("Rusty Lake Bundle", "Enigma", "+18", 96.32))
plataforma.adicionar_jogo_catalogo(Jogo("Slime rancher 2", "Casual", "Livre", 89.99 ))
plataforma.adicionar_jogo_catalogo(Jogo("Alice Madness Return", "Ação", "+14", 49.00 ))

print("\nCadastro do jogador:")
nickname = input("Digite o nickname: ")
id_jogador = int(input("Digite o ID do jogador: "))
saldo_inicial = float(input("Digite o saldo inicial: R$ "))

jogador_atual = Jogador(nickname, id_jogador, saldo_inicial)
plataforma.adicionar_jogador(jogador_atual)

while True:
    print("\n=== Menu ===")
    print("[1] Ver catálogo de jogos")
    print("[2] Ver perfil do jogador atual")
    print("[3] Comprar um jogo")
    print("[4] Adicionar saldo à carteira")
    print("[5] Buscar jogo por título")
    print("[6] Buscar jogador por ID e logar")
    print("[7] Cadastrar novo jogador")
    print("[0] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        plataforma.listar_jogos_catalogo()

    elif opcao == "2":
        jogador_atual.exibir_perfil()

    elif opcao == "3":
        plataforma.listar_jogos_catalogo()
        escolha = int(input("Digite o número do jogo que deseja comprar: ")) - 1
        if 0 <= escolha < len(plataforma.catalogo_de_jogos):
            jogo_escolhido = plataforma.catalogo_de_jogos[escolha]
            plataforma.realizar_compra(jogador_atual, jogo_escolhido)
        else:
            print("Escolha inválida.")

    elif opcao == "4":
        valor = float(input("Digite o valor para adicionar ao saldo: R$ "))
        jogador_atual.adicionar_saldo(valor)
        print("Saldo atualizado com sucesso!")

    elif opcao == "5":
        titulo = input("Digite o título do jogo: ")
        jogo = plataforma.buscar_jogo_por_titulo(titulo)
        if jogo:
            print("Jogo encontrado:")
            jogo.exibir_detalhes()
        else:
            print("Jogo não encontrado.")

    elif opcao == "6":
        id_busca = int(input("Digite o ID do jogador que deseja buscar: "))
        jogador_encontrado = plataforma.buscar_jogador_por_id(id_busca)
        if jogador_encontrado:
            print(f"Jogador encontrado: {jogador_encontrado.nickname}")
            escolha = input("Deseja logar com esse jogador? (s/n): ").lower()
            if escolha == "s":
                jogador_atual = jogador_encontrado
                print(f"Agora logado como: {jogador_atual.nickname}")
        else:
            print("Jogador não encontrado.")

    elif opcao == "7":
        print("\nCadastro de novo jogador:")
        nickname = input("Digite o nickname: ")
        id_jogador = int(input("Digite o ID do jogador: "))
        saldo_inicial = float(input("Digite o saldo inicial: R$ "))
        novo_jogador = Jogador(nickname, id_jogador, saldo_inicial)
        plataforma.adicionar_jogador(novo_jogador)
        print("Jogador cadastrado com sucesso!")

    elif opcao == "0":
        print("Encerrando o programa. Até mais!")
        break

    else:
        print("Opção inválida.")