class SomaSub: 
    def soma(self, a, b): #metodo/Função; o que ela faz
        soma = a + b
        self.soma = soma

    def sub(self, a, b): #metodo/Função; o que ela faz
        sub = a - b
        self.sub = sub

    def apresentar(self): #metodo/Função; o que ela faz
        print(f"Soma: {self.soma}")
        print(f"sub : {self.sub}")

cal = SomaSub() #é um objeto da classe SomaSub; e o self representa ele
cal.soma(20, 30) #chamada de cada método para o objeto cal
cal.sub(20, 30)
cal.apresentar()