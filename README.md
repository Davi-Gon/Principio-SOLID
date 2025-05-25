# Principio-SOLID
  SOLID são principios de programação orientada a objetos(POO) que servem para criar programas bem estruturados, robustos, flexiveis e de facil manutenção, em vista disso, podemos dizer que SOLID é de extrema importancia para um bom desenvolvimento.
  A sigla SOLID repesenta cinco principios a serem seguidos:  
  
S - Single Responsibility Principle;  
O - Open/Closed Principle;  
L - Liskov Substitution Principle;  
I - Interface Segregation Principle;  
D- Dependency Inversion Principle.  

  Para esse trabalho foi escolhido os principios S, O, L e I para ser dissertado sobre.  
### SRP - Single Responsibility Principle(Principio de Responsabilidade Unica):  
Esse Principio dita que uma classe pode ter apenas uma responsabilidade, ou seja, executar uma unica tarefa dentro do código. É comum a existencia de GOD Class's, Classes que fazem ou sabem demais, isso implica em um problema de manutenção e modificação, afinal é o mesmo que mexer em um emaranhado de fios, é confuso e as chances de dar errado é altissima, é ai que surje a SRP. A SRP impede a falta de coesão, o alto acoplamentro (muitas dependências), e a dificuldade que reaproveitar o código pois todos estão separados e exucutando a sua (única)função, melhorando até mesmo a legibilidade do código.

```
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
```



### OCP - Open/Closed Principle(Principio Aberto/Fechado):  
O principio OCP diz que "Obejetos ou entidades devem estar abertas para extensão, mas fechadas para modificação", digamos que você precise criar uma nova ligação de energia,  concordamos que é extremamente mais fácil fazer uma ligação/puxar de um ponto ja existente doque desmontar o quadro de energia inteiro para adicionala, afinal, quem garante que sera a ultima ligação a ser criada ? O principio OCP nos diz "exatamente" isso. 

```
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

```

### LSP - Liskov Substitution Principle(Principio da Substituição de Liskov):  
"Uma classe derivada deve ser substituivel por sua classe base" em um breve resumo, caso eu precise usar um componente que tem sua origem de outro componente, a maquina deve funcionar da mesma forma, sem precisar fazer modificações, afinal, um componente veio de outro. Esse principio para ser seguido de forma correta é precisso de outros principios de SOLID como o OCP.  

```
class A:
    def get_nome(self):
        print("Meu nome é A")

class B(A):
    def get_nome(self):
        print("Meu nome é B")

def imprime_nome(objeto: A):
    objeto.get_nome()

objeto1 = A()
objeto2 = B()

imprime_nome(objeto1)  # Meu nome é A
imprime_nome(objeto2)  # Meu nome é B
```

### ISP - Interface Segregation Principle(Principio da Segregação da Interface):  
Esse principio visa a não inutilidade "Uma classe não deve ser forçada a implementar interfaces e métodos que não irão utilizar", as interfaces devem ser especificas ao invés de genéricas. Quando criamos uma interface de comportamento por exemplo, podemos abstrair de forma que "todos os seres teram os mesmo comportamentos", porém é nitido que a classe pessoa não vai ter o mesmo comportamento que a classe cachorro, porém pode haver semelhanças, logo, alguns comportamentos não seram utilizados em uma classe, assim sendo -> inutil.

```
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
```
