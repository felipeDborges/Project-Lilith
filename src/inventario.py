from tkinter import *
from estilo import limpar_frame, adicionar_texto, criar_botoes, imagem_de_fundo, janela, frame_rolavel
import tkinter as tk

itens_inventario = {}

def adicionar_item(item):
    """Adiciona um item ao inventário ou incrementa a quantidade se já existir."""
    if item in itens_inventario:
        # Incrementa a quantidade se o item já existir
        itens_inventario[item] += 1
    else:
        # Se o item não existir, adiciona ele com quantidade 1
        itens_inventario[item] = 1

def exibir_inventario():
    limpar_frame(frame_rolavel)
    global frame_inventario
    frame_inventario = tk.Frame(frame_rolavel, bg='#2C2F33', bd=5, relief='groove')
    frame_inventario.grid(padx=10, pady=10)  # Adiciona margem ao redor do frame

    # Adiciona título ao inventário
    adicionar_texto(frame_inventario, "Inventário Delacruz", row=0, fonte_tamanho=18, cor_texto='#ADD8E6')

    # Adiciona os itens do inventário ou exibe mensagem se vazio
    if not itens_inventario:
        adicionar_texto(frame_inventario, "O inventário está vazio.", row=1, fonte_tamanho=14, cor_texto='#FF4500')
    else:
        for index, (item, quantidade) in enumerate(itens_inventario.items()):
            # Cria um frame para cada item com um contorno
            frame_item = tk.Frame(frame_inventario, bg='#2C2F33', bd=3, relief='groove')
            frame_item.grid(padx=5, pady=5, sticky='nsew')

            # Adiciona o item ao frame do item
            adicionar_texto(frame_item, f"{item} x{quantidade}", row=0)

exibir_inventario()