# Bibliotecas para dar uma brincada
import time 

def digitar(texto, delay=0.05):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Pula linha no final


# PARTE 1 - MODELANDO O JOGO

jogador_atual = None

class Jogo:
    def __init__(self, titulo, genero, classificacao_etaria, preco):
        self.titulo = titulo
        self.genero = genero
        self.classificacao_etaria = classificacao_etaria
        self.preco = preco
        self.avaliacoes = []

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Gênero: {self.genero}")
        print(f"Classificação Etária: {self.classificacao_etaria}")
        print(f"Preço: R$ {self.preco:.2f}")
        if self.avaliacoes:
            print(f"Avaliação média: {self.media_avaliacoes():.1f} / 5")
        print("-" * 30)

    def avaliar(self, nota):
        if 1 <= nota <= 5:
            self.avaliacoes.append(nota)
        else:
            print("Nota inválida. Use valores entre 1 e 5.")

    def media_avaliacoes(self):
        if self.avaliacoes:
            return sum(self.avaliacoes) / len(self.avaliacoes)
        return 0


# PARTE 2 - MODELANDO O JOGADOR

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


# PARTE 3 - MODELANDO A PLATAFORMA DE JOGOS

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

    def presentear_jogo(self, id_jogador_doador, id_jogador_receptor, titulo_jogo):
        doador = self.buscar_jogador_por_id(id_jogador_doador)
        receptor = self.buscar_jogador_por_id(id_jogador_receptor)
        jogo = self.buscar_jogo_por_titulo(titulo_jogo)
        if doador and receptor and jogo:
            if jogo in doador.biblioteca_de_jogos:
                doador.biblioteca_de_jogos.remove(jogo)
                receptor.adicionar_jogo_biblioteca(jogo)
                print(f"{doador.nickname} presenteou {receptor.nickname} com o jogo {jogo.titulo}!")
            else:
                print("O doador não possui este jogo.")
        else:
            print("Jogador doador, receptor ou jogo não encontrado.")


# PARTE 4 - TESTES E SIMULAÇÕES

plataforma = PlataformaDeJogos("GAMEPASS")

plataforma.adicionar_jogo_catalogo(Jogo("Minecraft", "SandBox", "Livre", 74.95))
plataforma.adicionar_jogo_catalogo(Jogo("Far Cry 4", "Ação", "18+", 74.95))
plataforma.adicionar_jogo_catalogo(Jogo("Duna", "Sobrevivência", "Livre", 39.90))
plataforma.adicionar_jogo_catalogo(Jogo("Call of Duty: Warzone", "FPS", "18+", 0.99))
plataforma.adicionar_jogo_catalogo(Jogo("Rusty Lake Bundle", "Enigma", "+18", 96.32))
plataforma.adicionar_jogo_catalogo(Jogo("Slime Rancher 2", "Casual", "Livre", 89.99))
plataforma.adicionar_jogo_catalogo(Jogo("Alice Madness Return", "Ação", "+14", 49.00))

# MENU INICIAL – Cadastro ou Login obrigatório
while jogador_atual is None:
    digitar("\033[34m\n============= Bem-vindo ao GAMEPASS =============\033[0m", delay=0.07)
    print("""
            [1] Cadastrar novo jogador
            [2] Logar com jogador existente
            [0] Sair
    """)

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nickname = input("Digite o nickname: ")
        id_jogador = int(input("Digite o ID do jogador: "))
        saldo_inicial = float(input("Digite o saldo inicial: R$ "))
        novo_jogador = Jogador(nickname, id_jogador, saldo_inicial)
        plataforma.adicionar_jogador(novo_jogador)
        jogador_atual = novo_jogador
        print(f"Jogador {nickname} cadastrado e logado com sucesso!")

    elif escolha == "2":
        id_busca = int(input("Digite o ID do jogador: "))
        jogador_encontrado = plataforma.buscar_jogador_por_id(id_busca)
        if jogador_encontrado:
            jogador_atual = jogador_encontrado
            print(f"Jogador {jogador_atual.nickname} logado com sucesso!")
        else:
            print("Jogador não encontrado.")

    elif escolha == "0":
        digitar("Saindo da plataforma. Até logo!", delay=0.07)
        exit()

    else:
        print("""\033[31mOPÇÃO INVÁLIDA\033[0m""")

# MENU PRINCIPAL
while True:
    print("\n=== Menu ===")
    print("[1] Ver catálogo de jogos")
    print("[2] Ver perfil do jogador atual")
    print("[3] Comprar um jogo")
    print("[4] Adicionar saldo à carteira")
    print("[5] Buscar jogo por título")
    print("[6] Buscar jogador por ID e logar")
    print("[7] Cadastrar novo jogador")
    print("[8] Presentear um jogo para outro jogador")
    print("[9] Avaliar um jogo")
    print("[0] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        plataforma.listar_jogos_catalogo()

    elif opcao == "2":
        jogador_atual.exibir_perfil()

    elif opcao == "3":
        carrinho = []

        while True:
            print("\n=== Menu do Carrinho ===")
            print("[1] Adicionar jogo ao carrinho")
            print("[2] Remover jogo do carrinho")
            print("[3] Ver carrinho")
            print("[0] Finalizar compra")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                plataforma.listar_jogos_catalogo()
                indice = int(input("Digite o número do jogo que deseja adicionar: ")) - 1
                if 0 <= indice < len(plataforma.catalogo_de_jogos):
                    jogo = plataforma.catalogo_de_jogos[indice]
                    if jogo in jogador_atual.biblioteca_de_jogos:
                        print("Você já possui este jogo.")
                    elif jogo in carrinho:
                        print("Este jogo já está no carrinho.")
                    else:
                        carrinho.append(jogo)
                        print(f"{jogo.titulo} adicionado ao carrinho.")
                else:
                    print("Escolha inválida.")

            elif escolha == "2":
                if not carrinho:
                    print("Carrinho está vazio.")
                else:
                    print("\n=== Jogos no Carrinho ===")
                    for idx, jogo in enumerate(carrinho, 1):
                        print(f"[{idx}] {jogo.titulo} - R$ {jogo.preco:.2f}")
                    indice = int(input("Digite o número do jogo para remover: ")) - 1
                    if 0 <= indice < len(carrinho):
                        removido = carrinho.pop(indice)
                        print(f"{removido.titulo} removido do carrinho.")
                    else:
                        print("Índice inválido.")

            elif escolha == "3":
                if not carrinho:
                    print("Carrinho está vazio.")
                else:
                    print("\n=== Carrinho de Compras ===")
                    for jogo in carrinho:
                        print(f"- {jogo.titulo} (R$ {jogo.preco:.2f})")
                    total = sum(jogo.preco for jogo in carrinho)
                    print(f"Total: R$ {total:.2f}")

            elif escolha == "0":
                if not carrinho:
                    print("Carrinho vazio. Nenhuma compra realizada.")
                else:
                    total = sum(jogo.preco for jogo in carrinho)
                    print("\nResumo do Carrinho:")
                    for jogo in carrinho:
                        print(f"- {jogo.titulo} (R$ {jogo.preco:.2f})")
                    print(f"Total: R$ {total:.2f}")
                    confirmar = input("Deseja finalizar a compra? (s/n): ").lower()
                    if confirmar == "s":
                        if jogador_atual.saldo_carteira >= total:
                            for jogo in carrinho:
                                jogador_atual.debitar_saldo(jogo.preco)
                                jogador_atual.adicionar_jogo_biblioteca(jogo)
                            print("Compra realizada com sucesso!")
                        else:
                            print("Saldo insuficiente para comprar todos os jogos.")
                    else:
                        print("Compra cancelada.")
                break

            else:
                print("Opção inválida.")

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

    elif opcao == "8":
        id_receptor = int(input("Digite o ID do jogador que vai receber o presente: "))
        titulo_jogo = input("Digite o título do jogo que deseja presentear: ")
        plataforma.presentear_jogo(jogador_atual.id_jogador, id_receptor, titulo_jogo)

    elif opcao == "9":
        titulo = input("Digite o título do jogo que deseja avaliar: ")
        jogo = plataforma.buscar_jogo_por_titulo(titulo)
        if jogo and jogo in jogador_atual.biblioteca_de_jogos:
            nota = int(input("Digite sua nota (1 a 5): "))
            jogo.avaliar(nota)
            print("Avaliação registrada com sucesso!")
        else:
            print("Jogo não encontrado na sua biblioteca.")

    elif opcao == "0":
        digitar("Saindo da plataforma. Até logo!", delay=0.07)
        break

    else:
        print("Opção inválida.")


