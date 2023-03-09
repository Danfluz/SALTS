import datetime

def calc_saida(entrada, dias=30):
    if type(dias) == str:
        dias = int(dias)
    if entrada.count('/') == 0:
        if len(entrada) == 8 and entrada.isnumeric():
            entrada = list(entrada)
            entrada.insert(2,'/')
            entrada.insert(5,'/')
            entrada = ''.join(entrada)

    if entrada.count('/') == 2:
        entrada = entrada.split('/')
        entrada[0] = int(entrada[0])
        entrada[1] = int(entrada[1])
        entrada[2] = int(entrada[2])

    while dias != 0:
        mes = entrada[1]
        if mes < 8 and (mes % 2) == 1:
            limite = 31
        elif mes > 7 and (mes % 2) == 0:
            limite = 31
        else:
            limite = 30
        if mes == 2:
            bissextos = [2024, 2028, 2032, 2036, 2040, 2044, 2048]
            if entrada[2] in bissextos:
                limite = 29 # ano bissexto (2024)
            else:
                limite = 28

        m_limite = 12

        entrada[0] +=1

        if entrada[0] > limite:
            entrada[0] = 1
            entrada[1] +=1

        if entrada[1] > m_limite:
            entrada[1] = 1
            entrada[2] +=1

        dias -=1

    if len(str(entrada[0])) != 2:
        entrada[0] = '0' + str(entrada[0])
    else:
        entrada[0] = str(entrada[0])

    if len(str(entrada[1])) != 2:
        entrada[1] = '0' + str(entrada[1])
    else:
        entrada[1] = str(entrada[1])

    entrada[2] = str(entrada[2])
    entrada.insert(1, '/')
    entrada.insert(3, '/')
    saida = ''.join(entrada)
    return saida

def calc_restantes(saida):
    saida = saida.split('/')
    presente = datetime.datetime.now()
    futuro = datetime.datetime(year=int(saida[2]), month=int(saida[1]), day=int(saida[0]), hour=23)
    restante = str(futuro - presente).split(' ')[0]

    return int(restante)

def salvar(listavalores):
    txt = open('bd', 'w')
    txt.write(str(listavalores))
    txt.close()

    return 'ok'

def carregar():
    txt = open('bd', 'r')
    texto = txt.read()
    txt.close()
    lista = eval(texto)

    return lista

def atualizar_dias(listavalores):
    for lista in listavalores:
        lista[-1] = calc_restantes(lista[-2])