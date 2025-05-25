''' Um progrma que recomenda o tamanho do alojamneto de um petshop(levando em conta somente uma variavel para exemplo)
 Tal petshop apenas trabalhava com cachorros, porém começou a trabalhar com gatos, levando em conta o sistema atual
 seria necessario fazer modificações o que infringe o principio OCP.
'''
class Dog():
    def __init__(self, nome, tamanho, raca, idade):
        self.nome = nome
        self.tamanho = tamanho
        self.raca = raca
        self.idade = idade

class AlojamentoRecomendado():
    def tamanhoAlojamento(self, dog):
        if dog.tamanho.lower() == "pequeno":
            return "Alojamento pequeno"
        elif dog.tamanho.lower() == "medio":
            return "Alojamento medio"
        else:
            return "Alojamento grande"

cliente1 = Dog("Rex", "Medio", "Labrador", 10)
alojamento = AlojamentoRecomendado()

recomendação = alojamento.tamanhoAlojamento(cliente1)
print(f"Alojamento recomendado para {cliente1.nome}: {recomendação}") 

''' Código arrumado para o principio OCP:
 Uma interface foi adicionada, pois agora qualquer nova adição extende da classe animal, sem precisar fazer
 modificações.
'''
class Animal:
    def get_tamanho(self):
        pass

    def get_nome(self):
        pass


# Subclasse para cachorros
class Dog(Animal):
    def __init__(self, nome, tamanho, raca, idade):
        self.nome = nome
        self.tamanho = tamanho
        self.raca = raca
        self.idade = idade

    def get_tamanho(self):
        return self.tamanho

    def get_nome(self):
        return self.nome


# Subclasse para gatos
class Cat(Animal):
    def __init__(self, nome, tamanho, cor, idade):
        self.nome = nome
        self.tamanho = tamanho
        self.cor = cor
        self.idade = idade

    def get_tamanho(self):
        return self.tamanho

    def get_nome(self):
        return self.nome


# Classe responsável por recomendar o alojamento
class AlojamentoRecomendado:
    def tamanhoAlojamento(self, animal: Animal):
        tamanho = animal.get_tamanho().lower()

        if tamanho == "pequeno":
            return "Alojamento pequeno"
        elif tamanho == "medio":
            return "Alojamento medio"
        elif tamanho == "grande":
            return "Alojamento grande"
        else:
            return "Tamanho desconhecido"


# Testando com Dog e Cat
cliente1 = Dog("Rex", "Medio", "Labrador", 10)
cliente2 = Cat("Mia", "Pequeno", "Branco", 2)

alojamento = AlojamentoRecomendado()

print(f"Alojamento para {cliente1.get_nome()}: {alojamento.tamanhoAlojamento(cliente1)}")
print(f"Alojamento para {cliente2.get_nome()}: {alojamento.tamanhoAlojamento(cliente2)}")


    