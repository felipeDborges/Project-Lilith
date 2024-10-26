from tkinter import *
from estilo import limpar_frame, adicionar_texto, criar_botoes, imagem_de_fundo, janela, frame_rolavel
import tkinter as tk
from inventario import exibir_inventario

atributos_delacruz = {
    'INT': 2,
    'REF': 8,
    'TEC': 4,
    'AuCon': 8,
    'ATR': 7,
    'SOR': 2,
    'MOV': 8,
    'TCO': 7,
    'EMP': 4
}

pericias_delacruz = {
    'NO_COMB': 10,
    'NOTAR': 4,
    'ARM_CURTAS': 4,
    'BRIGA': 0,
    'ART_MAR': 5,
    'ARMEIRO': 4,
    'FUZIL': 8,
    'ATLE': 2,
    'SUB': 0,
    'FURT': 3,
    'PRI_SUS': 5,
    'MOTO': 3,
    'RES': 2
}

atributos_movimento_delacruz = {
    'VIT': atributos_delacruz['TCO'] + 10,
    'DINHEIRO': 1500,
    'Levantar': atributos_delacruz['TCO'] * 40,
    'Correr': atributos_delacruz['MOV'] * 3,
    'Saltar': (atributos_delacruz['MOV'] * 3) / 4 #Usando o valor de "Correr"
}

armadura_delacruz = {
    "CABECA": 0,
    "TORSO": 14,
    "BRACO_D": 34,
    "BRACO_E": 14,
    "PERNA_D": 20,
    "PERNA_E": 20
}

def calcular_MTC(TCO):
    if TCO == 2:
        return 0
    elif 2 < TCO <= 4:
        return -1
    elif 4 < TCO <= 7:
        return -2
    elif 7 < TCO <= 9:
        return -3
    elif TCO == 10:
        return -4
    else:
        return None 

def ficha_delacruz():
    try:
        limpar_frame(frame_rolavel)
        from chapter_2 import inicio_Capitulo2

        #Nome e Classe
        adicionar_texto(frame_rolavel, "Nome: Bruno Delacruz", fonte_tamanho=20, cor_texto= '#4682B4', row=0)
        adicionar_texto(frame_rolavel, "Classe: Solo", fonte_tamanho=17, cor_texto='#ADD8E6', row=1)
        
        #Atributos
        adicionar_texto(frame_rolavel, f"INT: {atributos_delacruz['INT']}", cor_texto='#008080', row=2)
        adicionar_texto(frame_rolavel, f"REF: {atributos_delacruz['REF']}", cor_texto='#008080', row=3)
        adicionar_texto(frame_rolavel, f"TEC: {atributos_delacruz['TEC']}", cor_texto='#008080', row=4)
        adicionar_texto(frame_rolavel, f"AuCon: {atributos_delacruz['AuCon']}", cor_texto='#008080', row=5)
        adicionar_texto(frame_rolavel, f"ATR: {atributos_delacruz['ATR']}", cor_texto='#008080', row=6)
        adicionar_texto(frame_rolavel, f"SOR: {atributos_delacruz['SOR']}", cor_texto='#008080', row=7)
        adicionar_texto(frame_rolavel, f"MOV: {atributos_delacruz['MOV']}", cor_texto='#008080', row=8)
        adicionar_texto(frame_rolavel, f"TCO: {atributos_delacruz['TCO']}", cor_texto='#008080', row=9)
        adicionar_texto(frame_rolavel, f"EMP: {atributos_delacruz['EMP']}", cor_texto='#008080', row=10)
        adicionar_texto(frame_rolavel, f"MOV: {atributos_movimento_delacruz['Levantar']}", cor_texto='#008080', row=11)
        adicionar_texto(frame_rolavel, f"TCO: {atributos_movimento_delacruz['Correr']}", cor_texto='#008080', row=12)
        adicionar_texto(frame_rolavel, f"EMP: {atributos_movimento_delacruz['Saltar']}", cor_texto='#008080', row=13)
        
        #Implantes e Dinheiro
        adicionar_texto(frame_rolavel, "Implantes:", fonte_tamanho=17, cor_texto='#ADD8E6', row=15)
        adicionar_texto(frame_rolavel, "Braço De Reposição Direito", cor_texto='#008080', row=16)
        adicionar_texto(frame_rolavel, "Blindagem (PB 20)", cor_texto='#008080', row=17)
        adicionar_texto(frame_rolavel, "Soqueira de Aço(1D6+2)", cor_texto='#008080', row=18)
        adicionar_texto(frame_rolavel, f"Dinheiro: {atributos_movimento_delacruz['DINHEIRO']}", cor_texto='Yellow', row=19)

        #Habilidade Especial
        adicionar_texto(frame_rolavel, "Habilidade Especial", fonte_tamanho=17, cor_texto='#ADD8E6', row=1, column=1)
        adicionar_texto(frame_rolavel, f"Noção de Combate: {pericias_delacruz['NO_COMB']}", cor_texto='#008080', row=2, column=1)
        
        #Pericias
        adicionar_texto(frame_rolavel, "Pericias", fonte_tamanho=17, cor_texto='#ADD8E6', row=4, column=1)
        adicionar_texto(frame_rolavel, f"Atenção/Notar: {pericias_delacruz['NOTAR']}", cor_texto='#008080', row=5, column=1)
        adicionar_texto(frame_rolavel, f"Armas Curtas: {pericias_delacruz['ARM_CURTAS']}", cor_texto='#008080', row=6, column=1)
        adicionar_texto(frame_rolavel, f"Briga: {pericias_delacruz['BRIGA']}", cor_texto='#008080', row=7, column=1)
        adicionar_texto(frame_rolavel, f"Artes Marciais: {pericias_delacruz['ART_MAR']}", cor_texto='#008080', row=8, column=1)
        adicionar_texto(frame_rolavel, f"Conhecimento de Armas: {pericias_delacruz['ARMEIRO']}", cor_texto='#008080', row=9, column=1)
        adicionar_texto(frame_rolavel, f"Fuzil: {pericias_delacruz['FUZIL']}", cor_texto='#008080', row=10, column=1)
        adicionar_texto(frame_rolavel, f"Atletismo: {pericias_delacruz['ATLE']}", cor_texto='#008080', row=11, column=1)
        adicionar_texto(frame_rolavel, f"Submetralhadora: {pericias_delacruz['SUB']}", cor_texto='#008080', row=12, column=1)
        adicionar_texto(frame_rolavel, f"Furtividade: {pericias_delacruz['FURT']}", cor_texto='#008080', row=13, column=1)
        adicionar_texto(frame_rolavel, f"Primeiros Socorros: {pericias_delacruz['PRI_SUS']}", cor_texto='#008080', row=14, column=1)
        adicionar_texto(frame_rolavel, f"Motocicleta: {pericias_delacruz['MOTO']}", cor_texto='#008080', row=15, column=1)
        adicionar_texto(frame_rolavel, f"Resistencia: {pericias_delacruz['RES']}", cor_texto='#008080', row=16, column=1)

        #Vida e Armadura
        adicionar_texto(frame_rolavel, "Vida e Armadura:", fonte_tamanho=17, cor_texto='#ADD8E6', row=4, column=3)
        adicionar_texto(frame_rolavel, f"VIDA: {atributos_movimento_delacruz['VIT']}", cor_texto='red', row=5, column=3)
        adicionar_texto(frame_rolavel, f"MTC: {calcular_MTC(atributos_delacruz['TCO'])}", cor_texto='#008080', row=5, column=4)
        adicionar_texto(frame_rolavel, f"Cabeça: {armadura_delacruz ['CABECA']}", cor_texto='#008080', row=6, column=3)
        adicionar_texto(frame_rolavel, f"Torso: {armadura_delacruz ['TORSO']}", cor_texto='#008080', row=7, column=3)
        adicionar_texto(frame_rolavel, f"Braço D: {armadura_delacruz ['BRACO_D']}", cor_texto='#008080', row=8, column=3)
        adicionar_texto(frame_rolavel, f"Braço E: {armadura_delacruz ['BRACO_E']}", cor_texto='#008080', row=9, column=3)
        adicionar_texto(frame_rolavel, f"Perna D: {armadura_delacruz ['PERNA_D']}", cor_texto='#008080', row=10, column=3)
        adicionar_texto(frame_rolavel, f"Perna E: {armadura_delacruz ['PERNA_E']}", cor_texto='#008080', row=11, column=3)

        #Botão
        opcoes = [
                {'texto': "Inventario", 'comando': exibir_inventario, 'row':20, 'column':1},
                {'texto': "Voltar", 'comando': inicio_Capitulo2, 'row':20, 'column':2}
        ]
        criar_botoes(opcoes, linha_inicial=1)
    except tk.TclError:
        print("A janela foi fechada")

