from classes import animal
from classes import pinguim
from classes import camaleao
from colorama import init, Fore

init()

try:

    # --------Instancia da Classe (Objetos)--------
    pingu = pinguim.Pinguim('Pinguim', 'Pingu', 'Ave', 'Imperador', 'Preto e Branco', 'Ovipara', 400.50, False)
    pascal = camaleao.Camaleao('Camaleão', 'Pascal', 'Reptel', 'Furcifer', 'Multicor', 'Oviparo', 280.75)
    animais = animal.BancoDeDadosAnimais

    dicioAnimal = {"Id": None, "Animal": None, "Nome": None, "Familia": None, "Especie": None,
                   "Cor": None, "Reprodução": None, "Preço": None}

    # xX-X CRIAR FOR para automatizar do banco X-Xx

    id = pingu.gera_id()

    Animais = (("Id", pingu.gera_id()), ("Animal", pingu.animal), ("Nome", pingu.nome), ("Familia", pingu.familia),
               ("Especie", pingu.especie), ("Cor", pingu.cor), ("Reprodução", pingu.reproducao),
               ("Preço", f'R$ {pingu.preco:.2f}'))

    # convertendo para dicionario

    dicionario = dict((y, x) for y, x in Animais)
    # print(type(dicionario))
    # print(dicionario['Id'])
    pesquisaQuand = 0
    # xX-X SISTEMA PARA CONSULTAR OS ANIMAIS (input) X-Xx

    pesquisa = 1
    while pesquisa != 0:
        verificacao = False
        while not verificacao:

            pesquisasQuand = input("Qual a quantidade de consultas você deseja fazer? ")
            verificacao = pesquisasQuand.isnumeric()

        i = 1
        lista = []
        listaIdentificadores = []
        while i <= int(pesquisasQuand) and pesquisa != 0:

            pesquisa = input("Escolha qual tipo de consulta vc deseja fazer: " + Fore.YELLOW + "\n"
                                                                                               "1- Id\t\t"
                                                                                               "2- Animal\t\t"
                                                                                               "3- Nome\t\t\t\t"
                                                                                               "4- Familia""\n"
                                                                                               "5- Especie\t"
                                                                                               "6- Cor\t\t\t"
                                                                                               "7- Reprodução\t\t"
                                                                                               "8- Preço\n\n" +
                             Fore.RESET + "APERTE 0 p/ Sair\n\nDigite Aqui: ")

            if pesquisa == '1':
                lista.append('Id')
                listaIdentificadores.append('Id')

            if pesquisa == '2':
                lista.append('Animal')
                listaIdentificadores.append('Animal')

            if pesquisa == '3':
                lista.append('Nome')
                listaIdentificadores.append('Nome')

            if pesquisa == '4':
                lista.append('Familia')
                listaIdentificadores.append('Familia')

            if pesquisa == '5':
                lista.append('Especie')
                listaIdentificadores.append('Especie')

            if pesquisa == '6':
                lista.append('Cor')
                listaIdentificadores.append('Cor')

            if pesquisa == '7':
                lista.append('Reprodução')
                listaIdentificadores.append('Reprodução')

            if pesquisa == '8':
                lista.append('Preço')
                listaIdentificadores.append('Preço')

            pesquisa = int(pesquisa)
            i = i + 1

        print("CONSULTA...\n")
        i2 = 0
        for valor in lista:
            print(f'{listaIdentificadores[i2]}: {dicionario[valor]}')
            i2 = i2 + 1
        # dicionario['Id']


except Exception as e:
    print(f'main: {e}')

# ("Id", pascal.gera_id()),
# ("Animal", pascal.animal),
# ("Nome", pascal.nome),
# ("Familia", pascal.familia),
# ("Especie", pascal.especie),
# ("Cor", pascal.cor),
# ("Reprodução", pascal.reproducao),
# ("Preço", f'R$ {pascal.preco:.2f}'))
