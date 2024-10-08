from tkinter import *
import tkinter as tk
import pygame
from pygame import mixer
from PIL import ImageTk, Image

def texto_narrador(janela, texto, wraplength , cor_fundo, cor_texto, tamanho_fonte):
    
    fonte = ('Space Mono', tamanho_fonte, 'italic')
    rotulo = tk.Label(janela, text=texto, wraplength=wraplength, bg=cor_fundo, fg=cor_texto, font=fonte)
    return rotulo

pygame.mixer.init()
pygame.mixer.music.load('audio/Cyberpunk.ogg')
mixer.music.set_volume(0.1)
mixer.music.play(-1)



janela = tk.Tk()
janela.configure(bg='black')
janela.title("Project Lilith")
janela.geometry("1280x720")

imagem = Image.open('img/Inicio_Sonho.jpg')
nova_imagem = imagem.resize((720, 480))
imagem_tk = ImageTk.PhotoImage(nova_imagem)

label_imagem = Label(janela, image=imagem_tk)
label_imagem.pack()

frame_superior = tk.Frame(janela, bg='black')
frame_superior.pack(side='top')

frame_inferior = tk.Frame(janela, bg='black')
frame_inferior.pack(side='bottom')

inicio = texto_narrador(frame_superior, texto="Estamos no distante e distópico futuro de 2121, após os acontecimentos da Terceira Grande Guerra, o Brasil foi um dos poucos países que não sofreram ataques devastadores em seu território. Assim, o Novo Mexico e os poucos remanescentes do Japão se uniram ao brasil levando sua cultura e conhecimento a grande nação. Agora, Brasil lidera o mundo em suas pesquisas de aperfeiçoamento humano.\nUma dessas pesquisas se chama “Projeto Lilith”, uma arma nunca antes imaginada, que nossos protagonistas foram contratados para roubá-la, porém o que eles não esperavam era que essa simples missão se tornaria o estopim para o possível fim do mundo.", wraplength=1200, cor_fundo='black', cor_texto='#ADD8E6', tamanho_fonte=11)
inicio.pack(side="top", pady=20)

botao = tk.Button(frame_inferior, text="Acordar", bg='#4682B4', fg='#ADD8E6', font=('Space Mono', 9, 'italic'))
botao.pack(pady=(0, 60))

janela.mainloop()
