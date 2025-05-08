class Livro:
    def __init__(self, titulo, autor, numero_de_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_de_paginas = numero_de_paginas

    def detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.numero_de_paginas}")
        

lista_livros = []
contador = 0

while True:
    titulo = input("Título: ")
    autor = input("Autor: ")
    numero_de_paginas = int(input("Número de páginas: "))

    livro = Livro(titulo, autor, numero_de_paginas)
    lista_livros.append(livro)
    contador += 1

    continuar = input("Deseja adicionar outro livro? (s/n): ").lower()
    if continuar == 's':
        continue
    if continuar == 'n':
        break
    if continuar != 's' or 'n':
        print("Inválido!")
        continuar = input("Deseja adicionar outro livro? (s/n): ").lower()

print("\nLivros cadastrados:")
print(f"Total de livros cadastrados: {contador}\n")
for livro in lista_livros:
    livro.detalhes()
    print("\n")
