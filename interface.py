import PySimpleGUI as sg
from principal import *

try:
    listavalores = carregar()
except:
    listavalores = [['11111111','SD Feliciano', 'TESTE', '30', '06/03/2023', '06/04/2023', 30]]

atualizar_dias(listavalores)

def tlistas(lstvalores):
    sg.theme('SystemDefaultForReal')
    layout = [
        # [sg.Text('SALTS', font='Arial 15')],
        # [sg.Text('')],
        [sg.Text('SALTS', font='Arial 15'), sg.Text('Nome:'), sg.Input('',key='nome', size=(30,1)),sg.Text('Matrícula:'), sg.Input('',key='matricula', size=(15,1)), sg.Text('Processo (opc.):'), sg.Input('',key='processo', size=(15,1))],
        [sg.Text('',size=(0,1)), sg.Image('pmpelogo.png',subsample=7, pad=1), sg.Text('',size=(1,1)), sg.Text('Duração (dias):'), sg.Input('',key='dias', size=(12,1)),sg.Text('Entrada (dd/mm/aaaa):'), sg.Input('',key='entrada', size=(15,1)), sg.Text(' '*18), sg.Button('Adicionar'), sg.Button('Remover')],
        [sg.Text('')],
        [sg.Frame('LTS',layout=[[sg.Table(lstvalores,['Processo','Nome', 'Matricula', 'Duração (Dias)', 'Data Entrada', 'Data Saída', 'Dias restantes'], size=(20,20),auto_size_columns=False, col_widths=[12,20,12,12,12,12,11],justification='center',key='lts')]])],
        [sg.Text('SALTS - Sistema de Acompanhamento de Licença para Tratamento de Saúde'), sg.Text(' '*65), sg.Text('ver 1.1 por Dan F Luz', font='arial 8')],
    ]

    return sg.Window('SALTS', layout=layout, size=(880,512) , icon='pmpeico.ico',titlebar_icon='pmpelogo.ico')


janela = tlistas(listavalores)

while True:
    event, value = janela.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Adicionar':
        if value['dias'] == '' or value['matricula'] == '' or value['entrada'] == '' or value['nome'] == '':
            sg.popup('Preencha os campos necessarios')
        else:
            processo = value['processo']
            nome = value['nome']
            matricula = value['matricula']
            dias = value['dias']
            entrada = value['entrada']
            saida = calc_saida(entrada, dias)
            restantes = calc_restantes(saida)
            if not '/' in entrada:
                entrada = list(entrada)
                entrada.insert(2,'/')
                entrada.insert(5,'/')
                entrada = ''.join(entrada)
            listavalores.append([processo, nome, matricula, dias, entrada, saida, restantes])
            listavalores.sort(key=lambda x: x[-1])
            janela['lts'].update(values=listavalores)
            janela['nome'].update('')
            janela['matricula'].update('')
            janela['entrada'].update('')
            janela['dias'].update('')
            janela['processo'].update('')
            salvar(listavalores)

    if event == 'Remover':
        if value['lts'] == []:
            continue
        selecionado = value['lts'][0]
        listavalores.pop(selecionado)
        try:
            listavalores.sort(key=lambda x: x[-1])
        except:
            pass
        janela['lts'].update(values=listavalores)
        salvar(listavalores)


janela.close()