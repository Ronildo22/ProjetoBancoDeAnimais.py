from classes import animal
from classes import pinguim
from classes import camaleao

try:

    # --------Instancia da Classe (Objetos)--------
    pingu = pinguim.Pinguim('Pinguim', 'Pingu', 'Ave', 'Imperador', 'Preto e Branco', 'Ovipara', 400.50, False)
    pascal = camaleao.Camaleao('Camaleão', 'Pascal', 'Reptel', 'Furcifer', 'Multicor', 'Oviparo', 280.75)
    animais = animal.BancoDeDadosAnimais

    animais.listar_animais = {"Id": pingu.gera_id(), "Animal": pingu.animal, "Nome": pingu.nome,
                              "Familia": pingu.familia, "Especie": pingu.especie, "Cor": pingu.cor,
                              "Reprodução": pingu.reporducao, "Preço": f'R$ {pingu.preco:.2f}'},\
                             {"Id": pascal.gera_id(), "Animal": pascal.animal, "Nome": pascal.nome,
                              "Familia": pascal.familia, "Especie": pascal.especie, "Cor": pascal.cor,
                              "Reprodução": pascal.reporducao, "Preço": f'R$ {pascal.preco:.2f}'}

    #Fazer uma consulta do animal eseu preço

    print(animais.listar_animais)
    # print(animais.listar_animais[1])

except Exception as e:
    print(f'main: {e}')
