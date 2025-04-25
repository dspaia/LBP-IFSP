class Animal:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
        
        def emitir_som(self):
            print("Som genérico do animal!")
            
class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")
        
class Gato(Animal):
    def emitir_som(self):
        print("Miau!")
        
def fazer_som(animal):
    animal.emitir_som()
    
        
cachorro_nome, cachorro_idade = input("").split()
gato_nome, gato_idade = input("").split()
        
meu_cachorro = Cachorro(cachorro_nome, cachorro_idade)
meu_gato = Gato(gato_nome, gato_idade)


print(f"O nome do meu gato é {meu_gato.nome} , Ele tem {meu_gato.idade} anos. Ele quer falar com vocês, fala aí:")
meu_gato.emitir_som()

print(f"\nO nome do meu cachorro é {meu_cachorro.nome} , Ele tem {meu_cachorro.idade} anos. Ele quer falar com vocês, fala aí:", end=" ")
fazer_som(meu_cachorro)



