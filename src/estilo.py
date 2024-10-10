from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

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

    imagem = Image.open(caminho_imagem)
    nova_imagem = imagem.resize((720, 480))
    imagem_tk_global = ImageTk.PhotoImage(nova_imagem)
    label_imagem = tk.Label(janela, image=imagem_tk_global)
    label_imagem.pack()
    return label_imagem

def criar_interface():
    global janela, canvas, frame_rolavel

    janela = tk.Tk()
    janela.title("Project Lilith")    
    janela.geometry("1280x720")
    janela.configure(bg='black')

    # Canvas para Scroll
    canvas = tk.Canvas(janela, bg='black', highlightthickness=0)
    canvas.pack(side='left', fill='both', expand=True)

    # Frame que será rolado dentro do Canvas
    frame_rolavel = tk.Frame(canvas, bg='black')
    canvas.create_window((0, 0), window=frame_rolavel, anchor='nw')

    # Barra de Rolagem associada ao Canvas
    scrollbar = tk.Scrollbar(janela, orient='vertical', command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side='right', fill='y')

    # Configurar a rolagem do Frame
    frame_rolavel.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
#Iniciar Aplicação
criar_interface()