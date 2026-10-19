class cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
    def latir(self):
        print(self.nome, " diz: Au au!")
    def mostrarinfo(self):
        print("Nome: ", self.nome)
        print("Raça: ", self.raca)
        print("idade: ", self.idade, "\n")
cachorro1 = cachorro("Shake", "Pug", 9)
cachorro2 = cachorro("Roliço", "vira-lata", 8)
cachorro1.latir()
cachorro1.mostrarinfo()
cachorro2.latir()
cachorro2.mostrarinfo()
cachorro1.idade = 7
cachorro1.mostrarinfo()