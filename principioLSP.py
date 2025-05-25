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