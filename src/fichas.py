from tkinter import *
from estilo import limpar_frame, adicionar_texto, criar_botoes, imagem_de_fundo, janela, frame_rolavel
import tkinter as tk
from fichas import *
from chapter_2 import *

def alterar_imagem_de_fundo(frame, caminho_imagem):
    imagem_de_fundo(frame, caminho_imagem)

def ficha_delacruz():
    #Nova de fundo
    limpar_frame(frame_rolavel)

    alterar_imagem_de_fundo(frame_rolavel, 'img/Capitulo_2.jpg')

    texto_inicial = ("Você esta com sua parceira androide e seu cachorro robo Salsicha, vocês chegaram ao ponto de encontro que o Espinosa marcou, o Pinto Seco. "
                     "Vocês não sabem qual missão ele irá oferecer para vocês, a unica informação é o pagamento,")
    adicionar_texto(frame_rolavel, texto_inicial, row=1)
    adicionar_texto(frame_rolavel, "R$ 1.500.000,00", fonte_tamanho=11, cor_texto='#00FF00', row=1)

    #Botão
    botao_inicial = tk.Button(frame_rolavel, text="Acordar", bg='#4682B4', fg='#ADD8E6', 
                font=('Space Mono', 9, 'italic'), command= inicio_Capitulo2)
    botao_inicial.grid(row=2, column=0, padx=10, pady=10)

ficha_delacruz()