from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import pygame
from pygame import mixer

imagem_tk_global = None

def criar_interface():
    global janela, canvas, frame_rolavel

    janela = tk.Tk()
    janela.title("Project Lilith")    
    janela.geometry("1280x720")
    janela.configure(bg='black')

    # Criação do Canvas
    canvas = tk.Canvas(janela, bg='black')
    canvas.pack(side='left', fill='both', expand=True)

    # Criação da barra de rolagem
    scrollbar = tk.Scrollbar(janela, orient='vertical', command=canvas.yview)
    scrollbar.pack(side='right', fill='y')

    # Criação do Frame que será rolado dentro do Canvas
    frame_rolavel = tk.Frame(canvas, bg='black')
    canvas.create_window((0, 0), window=frame_rolavel, anchor='nw')

    # Configuração do Canvas para usar a barra de rolagem
    canvas.configure(yscrollcommand=scrollbar.set)

    # Atualiza a scrollregion
    frame_rolavel.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    #Áudio
    pygame.mixer.init()
    pygame.mixer.music.load('audio/Cyberpunk.ogg')
    mixer.music.set_volume(0.1)
    mixer.music.play(-1)

def limpar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def imagem_de_fundo(frame, caminho_imagem):
    #Imagem de fundo
    global imagem_tk_global

    imagem = Image.open(caminho_imagem)
    nova_imagem = imagem.resize((720, 480))
    imagem_tk_global = ImageTk.PhotoImage(nova_imagem)

    label_imagem = tk.Label(frame, image=imagem_tk_global, bg='black')
    label_imagem.grid(row=0, column=0, sticky='nsew')

def adicionar_texto(frame, texto, row, column=0, fonte_tamanho=11, cor_texto='#ADD8E6', cor_fundo='black'):
    novo_texto = tk.Label(frame, text=texto, wraplength=1000, justify='center' ,
                          fg=cor_texto, bg=cor_fundo, font=('Space Mono', fonte_tamanho, 'italic'),
                          anchor='center')
    novo_texto.grid(column=column, row=row, sticky='nsew')
    frame.grid_columnconfigure(column, weight=1)
    return novo_texto

def criar_botoes(opcoes, linha_inicial, column=0):
    linha = linha_inicial

    for opcao in opcoes:
        cor_fundo = opcao.get('bg', '#4682B4')  # Cor de fundo padrão
        cor_texto = opcao.get('fg', '#ADD8E6')  # Cor do texto padrão

        botao = tk.Button(frame_rolavel, text=opcao['texto'], bg=cor_fundo, fg=cor_texto, 
                            font=('Space Mono', 9, 'italic'), command=opcao['comando'])
        
        linha_inicial = opcao.get('row', linha)
        coluna_botao = opcao.get('column', column)

        botao.grid(row=linha_inicial, column=coluna_botao, padx=10, pady=10)
        if 'row' not in opcao:
            linha += 2

   
#Iniciar Aplicação
criar_interface()