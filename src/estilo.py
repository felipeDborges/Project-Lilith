from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import pygame
from pygame import mixer

imagem_tk_global = None

def limpar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def adicionar_texto(frame, texto, fonte_tamanho=11, cor_texto='#ADD8E6', cor_fundo='black'):
    novo_texto = tk.Label(frame, text=texto, wraplength=1000, 
                          fg=cor_texto, bg=cor_fundo, font=('Space Mono', fonte_tamanho, 'italic'),
                          anchor='center')
    novo_texto.pack(pady=10)
    return novo_texto

def criar_botoes(opcoes):

    for opcao in opcoes:
        botao = tk.Button(frame_rolavel, text=opcao['texto'], bg='#4682B4', fg='#ADD8E6', 
                            font=('Space Mono', 9, 'italic'), command=opcao['comando'])
        botao.pack(pady=20, anchor='center')

def imagem_de_fundo(janela, caminho_imagem):
    #Imagem de fundo
    global imagem_tk_global
    try:
        imagem = Image.open(caminho_imagem)
        nova_imagem = imagem.resize((720, 480))
        imagem_tk_global = ImageTk.PhotoImage(nova_imagem)
        # Exibe a imagem no canvas ou no frame
        label_imagem = tk.Label(janela, image=imagem_tk_global, bg='black')
        label_imagem.pack(fill='both', expand=True)

        # Atualiza a interface para garantir que a imagem apareça
        janela.update_idletasks()
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")

def criar_interface():
    global janela, canvas, frame_rolavel

    janela = tk.Tk()
    janela.title("Project Lilith")    
    janela.geometry("1280x720")
    janela.configure(bg='black')

    # Canvas para Scroll
    canvas = tk.Canvas(janela, bg='black', highlightthickness=0)
    canvas.pack(side='bottom', fill='both', expand=True)

    # Frame que será rolado dentro do Canvas
    frame_rolavel = tk.Frame(canvas, bg='black')
    canvas.create_window((0, 0), window=frame_rolavel, anchor='nw')

    # Barra de Rolagem associada ao Canvas
    scrollbar = tk.Scrollbar(janela, orient='vertical', command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side='right', fill='y')

    # Configurar a rolagem do Frame
    frame_rolavel.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    #Áudio
    pygame.mixer.init()
    pygame.mixer.music.load('audio/Cyberpunk.ogg')
    mixer.music.set_volume(0.1)
    mixer.music.play(-1)
    
#Iniciar Aplicação
criar_interface()