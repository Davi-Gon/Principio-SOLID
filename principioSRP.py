# Uma classe que tem 2 responsabilidades -> operações matematicas e apresentação dos resuldados
class SomaSub: 
    def soma(self, a, b):
        soma = a + b
        self.soma = soma

    def sub(self, a, b):
        sub = a - b
        self.sub = sub

    def apresentar(self):
        print(f"Soma: {self.soma}")
        print(f"sub : {self.sub}")

# Sendo assim não segue o principio SRP
cal = SomaSub()
cal.soma(20, 30)
cal.sub(20, 30)
cal.apresentar()


# Para aplicar o SRP as seguintes mudanças são necessarias:
# A classe somasub apenas realiza as operações:
class SomaSub:

    def soma(self, a, b):
        self.soma = a + b

    def sub(self, a, b):
        self.sub = a - b

# É criada outra classe para a Apresentação
class Apresentador:
    def apresentar(self, operacoes):
        print(f"Soma: {operacoes.soma}")
        print(f"Sub : {operacoes.sub}")


# Uso:
op = SomaSub()
op.soma(20, 30)
op.sub(20, 30)

apresentador = Apresentador()
apresentador.apresentar(op)