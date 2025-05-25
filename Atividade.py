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

cal = SomaSub()
cal.soma(20, 30)
cal.sub(20, 30)
cal.apresentar()
