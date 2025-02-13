class Pessoa:
    nome = "Eu"
    idade = 0
    peso = 0
    altura = 0

    def envelhecer(self, valor):
        self.idade += valor

    def engordar(self, valor):
        self.peso += valor

    def emagrecer(self, valor):
        if (self.peso >= valor):
            self.peso -= valor
        else:
            print("Peso incorreto")

    def crescer(self, valor):
        self.altura += valor
    
if __name__ == '__main__':
    pessoa = Pessoa()
    pessoa.altura = 1.80
    pessoa.peso = 70
    pessoa.idade = 20
    pessoa.crescer(0.05)
    pessoa.envelhecer(1)
    pessoa.engordar(2)
    print(pessoa.nome)
    print(pessoa.idade)
    print(pessoa.peso)
    print(pessoa.altura)