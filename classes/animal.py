import random

try:

    class BancoDeDadosAnimais:

        # Atributos do Metodo
        anoAtual = '2023'

        # Metodo construtor OU Metodo de instancia
        def __init__(self, nome, preco):
            self.__nome = nome
            self.__preco = preco
            self.__listaAnimal = {}

        # --- Set/Get os "self." que vc inseriu com os "@" (decoradores) abaixo ---
        # X---Melhor para trabalhar com Encapsolamento ---X

        # Getter
        @property
        def preco(self):
            return self.__preco

        # Setter
        @preco.setter
        def preco(self, valor):
            self.__preco = valor

        # X-- Vai trazer apenas o "self.__nome" instanciodo no objeto
        #           (por conta do private do Encapsolamento) --X

        def __nome_animal(self):
            print(f'O nome do animal é {self.__nome}')

        # Metodo usado para trabalhar com atributos da classe

        @classmethod
        def ano_nascimento(cls, ano_nascimento: int):
            idade = int(cls.anoAtual) - ano_nascimento
            return idade

        # Metodo usado para coisas fixas que nao vão mudar

        @staticmethod
        def gera_id():

            # xX-X Fazer um Auto Incremento para gerar um Id corretamente X-Xx

            id = random.randint(1, 100)
            return id

    # instanciando o objeto
    # bd = BancoDeDadosAnimais('João', 50.0)

    # # class do metodo
    # print(f'Metodo Class:  {bd.ano_nascimento(2003)}')

    # # static metodo
    # print(f'Static: {bd.gera_id()}')

    # # setter
    # bd.preco = 'Ronaldo'

    # get
    # print(f'Getter {bd.preco}')


except Exception as e:
    print(f'animal: {e}')
