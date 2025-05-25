# Um exemplo que infringe o ISP:
# A interface Animal obriga todos os animais a implementarem todos os métodos, mesmo que não façam sentido

class Animal:
    def comer(self):
        pass

    def voar(self):
        pass

class Cachorro(Animal):
    def comer(self):
        return "Cachorro comendo"

    def voar(self):
        return "Erro: cachorro não voa"  # Não faz sentido

class Passaro(Animal):
    def comer(self):
        return "Pássaro comendo"

    def voar(self):
        return "Pássaro voando"

# Uso
print(Cachorro().voar())  # Isso não deveria existir

 #Agora cada interface representa uma habilidade separada

class Comedor:
    def comer(self):
        pass

class Voador:
    def voar(self):
        pass

class Cachorro(Comedor):
    def comer(self):
        return "Cachorro comendo"

class Passaro(Comedor, Voador):
    def comer(self):
        return "Pássaro comendo"

    def voar(self):
        return "Pássaro voando"

# Uso
dog = Cachorro()
bird = Passaro()

print(dog.comer())
print(bird.comer())
print(bird.voar())