from classes import passaro

try:

    class Pinguim(passaro.Passaro):

        def __init__(self, animal, nome, familia, especie, cor, reproducao, preco: float, voa: bool):
            super().__init__(nome, preco, voa)
            self.animal = animal
            self.nome = nome
            self.familia = familia
            self.especie = especie
            self.cor = cor
            self.reporducao = reproducao
            self.voa = voa

        def comer(self):
            print(f'O pinguin {self.nome} está COMENDO')

        def voar(self):
            if self.voa:
                print("Esse passaro voa!!")
            else:
                print("Esse passaro NAO voa!!")


except Exception as e:
    print(f'pinguim: {e}')
