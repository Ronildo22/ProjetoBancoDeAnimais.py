from classes import repteis

try:

    class Camaleao(repteis.Repteis):
        def __init__(self, animal, nome, familia, especie, cor, reproducao, preco: float):
            super().__init__(nome, preco)
            self.animal = animal
            self.nome = nome
            self.familia = familia
            self.especie = especie
            self.cor = cor
            self.reproducao = reproducao


except Exception as e:
    print(f'Camaleao: {e}')
