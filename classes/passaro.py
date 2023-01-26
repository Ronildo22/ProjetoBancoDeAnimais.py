from classes import animal

try:

    class Passaro(animal.BancoDeDadosAnimais):

        def __init__(self, nome, preco, voa: bool):
            super().__init__(nome, preco)
            self.voa = voa


except Exception as e:
    print(f'passaro: {e}')
