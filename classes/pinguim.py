from classes import passaro

try:

    class Pinguim(passaro.Passaro):

        def __init__(self, animal, nome, familia, especie, cor, reproducao, preco, voa: bool):
            super().__init__(nome, preco, voa)
            self.animal = animal
            self.nome = nome
            self.familia = familia
            self.especie = especie
            self.cor = cor
            self.reproducao = reproducao
            self.voa = voa


except Exception as e:
    print(f'pinguim: {e}')
