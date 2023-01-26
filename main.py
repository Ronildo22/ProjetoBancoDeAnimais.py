from classes import animal
from classes import pinguim
from classes import camaleao
from colorama import init, Fore
import locale

init()

try:

    # xX-X CRIAR FOR para automatizar do banco X-Xx

    # --------Instancia da Classe (Objetos)--------

    pingu = pinguim.Pinguim('Pinguim', 'Pingu', 'Ave', 'Imperador', 'Preto e Branco', 'Oviparo', 1200.50, False)
    pascal = camaleao.Camaleao('Camaleão', 'Pascal', 'Reptel', 'Furcifer', 'Multicor', 'Oviparo', 280.75)
    animais = animal.BancoDeDadosAnimais

    dadosPinguim = (("Id", pingu.gera_id()), ("Animal", pingu.animal), ("Nome", pingu.nome),
                    ("Familia", pingu.familia), ("Especie", pingu.especie), ("Cor", pingu.cor),
                    ("Reprodução", pingu.reproducao), ("Preço", f'R$ {pingu.preco:.2f}'))

    dadosCamaleao = (("Id", pascal.gera_id()), ("Animal", pascal.animal), ("Nome", pascal.nome),
                     ("Familia", pascal.familia), ("Especie", pascal.especie), ("Cor", pascal.cor),
                     ("Reprodução", pascal.reproducao), ("Preço", f'R$ {pascal.preco:.2f}'))

    dictPingim = dict((y, x) for y, x in dadosPinguim)
    dictCamaleao = dict((y, x) for y, x in dadosCamaleao)

    pesquisaCaracteristicas = 1
    ancoraEscolha_animais = 1
    while pesquisaCaracteristicas != 0:
        verificacao = False
        verificacao2 = False
        while not verificacao:

            pesquisasQuand = input("\nQual a quantidade de consultas você deseja fazer?"
                                   "\n\nDIGITE 0 p/ Sair\n\nDigite Aqui: ")

            verificacao = pesquisasQuand.isnumeric()

            if pesquisasQuand == '0':
                exit()

        while not verificacao2:
            pesquisaAnimal = input("\nQual animal você deseja consultar: \n"
                                   "1- Piguim\n"
                                   "2- Camaleão\n\n"
                                   "DIGITE 0 p/ Sair\n\nDigite Aqui: ")

            if pesquisaAnimal == '1':
                tokenAnimal = 'pinguim'
                verificacao2 = pesquisaAnimal.isdigit()

            elif pesquisaAnimal == '2':
                tokenAnimal = 'camaleão'
                verificacao2 = pesquisaAnimal.isdigit()

            elif pesquisaAnimal == '0':
                exit()

            else:
                print(Fore.RED + '\nDigite um número reverente a consulta!!!' + Fore.RESET)

        i = 1
        listaConsulta = []
        listaIdentificadores = []
        indicadorConsultas = int(pesquisasQuand)

        while i <= int(pesquisasQuand) and pesquisaCaracteristicas != 0:

            print(f'\nQuantidade de consultas restantes: {indicadorConsultas}')

            pesquisaCaracteristicas = input("\nEscolha qual tipo de consulta vc deseja fazer: "
                                            + Fore.YELLOW + "\n""1- Id\t\t"
                                                                "2- Animal\t\t"
                                                                "3- Nome\t\t\t\t"
                                                                "4- Familia""\n"
                                                                "5- Especie\t"
                                                                "6- Cor\t\t\t"
                                                                "7- Reprodução\t\t"
                                                                "8- Preço\n\n" + Fore.RESET +
                                            "DIGITE 0 p/ Sair\n\nDigite Aqui: ")

            if pesquisaCaracteristicas == '1':
                listaConsulta.append('Id')
                listaIdentificadores.append('Id')

            elif pesquisaCaracteristicas == '2':
                listaConsulta.append('Animal')
                listaIdentificadores.append('Animal')

            elif pesquisaCaracteristicas == '3':
                listaConsulta.append('Nome')
                listaIdentificadores.append('Nome')

            elif pesquisaCaracteristicas == '4':
                listaConsulta.append('Familia')
                listaIdentificadores.append('Familia')

            elif pesquisaCaracteristicas == '5':
                listaConsulta.append('Especie')
                listaIdentificadores.append('Especie')

            elif pesquisaCaracteristicas == '6':
                listaConsulta.append('Cor')
                listaIdentificadores.append('Cor')

            elif pesquisaCaracteristicas == '7':
                listaConsulta.append('Reprodução')
                listaIdentificadores.append('Reprodução')

            elif pesquisaCaracteristicas == '8':
                listaConsulta.append('Preço')
                listaIdentificadores.append('Preço')

            else:
                if pesquisaCaracteristicas == '0':
                    pass
                else:
                    print(Fore.RED+'\nDigite um número reverente a consulta!!!'+Fore.RESET)
                    break

            pesquisaCaracteristicas = int(pesquisaCaracteristicas)
            i = i + 1
            indicadorConsultas = indicadorConsultas - 1

        print("CONSULTA...\n")
        i2 = 0


        if tokenAnimal == 'pinguim':

            for valor in listaConsulta:

                if valor == 'Preço':

                    # --convertendo o horario para o padrão brasileiro--
                    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
                    var = locale.currency(pingu.preco, grouping=True)
                    print(f'{listaIdentificadores[i2]}: {var}')

                else:
                    print(f'{listaIdentificadores[i2]}: {dictPingim[valor]}')

                i2 = i2 + 1

        if tokenAnimal == 'camaleão':

            for valor in listaConsulta:

                if valor == 'Preço':

                    # --convertendo o horario para o padrão brasileiro--
                    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
                    var = locale.currency(pingu.preco, grouping=True)
                    print(f'{listaIdentificadores[i2]}: {var}')

                else:
                    print(f'{listaIdentificadores[i2]}: {dictCamaleao[valor]}')

                i2 = i2 + 1


except Exception as e:
    print(f'main: {e}')
