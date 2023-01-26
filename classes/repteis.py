from classes import animal

try:

    class Repteis(animal.BancoDeDadosAnimais):
        def __init__(self, nome, preco):
            super().__init__(nome, preco)

except Exception as e:
    print(f'repteis: {e}')
