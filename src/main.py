from tkinter import *
import tkinter as tk
import pygame
from pygame import mixer
from PIL import ImageTk, Image
import estilo

def criar_interface():
    global janela, frame_superior, frame_inferior,label_imagem, imagem_tk, inicio_narrador, botao

    janela = tk.Tk()
    janela.title("Project Lilith")    
    janela.geometry("1280x720")
    janela.configure(bg='black')
  
    #Imagem de fundo
    imagem = Image.open('img/Inicio_Sonho.jpg')
    nova_imagem = imagem.resize((720, 480))
    imagem_tk = ImageTk.PhotoImage(nova_imagem)
    label_imagem = tk.Label(janela, image=imagem_tk)
    label_imagem.pack()

    #Frames
    frame_superior = tk.Frame(janela, bg='black')
    frame_superior.pack(side='top')
    frame_inferior = tk.Frame(janela, bg='black')
    frame_inferior.pack(side='bottom')

    #Rótulo inicial
    inicio_narrador = estilo.texto_narrador(frame_superior, texto="Estamos no distante e distópico futuro de 2121, após os acontecimentos da Terceira Grande Guerra, o Brasil foi um dos poucos países que não sofreram ataques devastadores em seu território. Assim, o Novo Mexico e os poucos remanescentes do Japão se uniram ao brasil levando sua cultura e conhecimento a grande nação. Agora, Brasil lidera o mundo em suas pesquisas de aperfeiçoamento humano.\nUma dessas pesquisas se chama “Projeto Lilith”, uma arma nunca antes imaginada, que nossos protagonistas foram contratados para roubá-la, porém o que eles não esperavam era que essa simples missão se tornaria o estopim para o possível fim do mundo.", 
                            wraplength=1200, cor_fundo='black', cor_texto='#ADD8E6', fonte_tamanho=11)
    inicio_narrador.pack(side="top", pady=20)

    #Botão
    botao = tk.Button(frame_inferior, text="Acordar", bg='#4682B4', fg='#ADD8E6', 
                font=('Space Mono', 9, 'italic'), command=despertar)
    botao.pack(pady=(0, 20))

    #Áudio
    pygame.mixer.init()
    pygame.mixer.music.load('audio/Cyberpunk.ogg')
    mixer.music.set_volume(0.1)
    mixer.music.play(-1)

def despertar():
    #Nova de fundo
    imagem = Image.open('img/Quarto.jpg')
    nova_imagem = imagem.resize((720, 480))
    imagem_tk = ImageTk.PhotoImage(nova_imagem)
    label_imagem.config(image=imagem_tk)
    label_imagem.image = imagem_tk

    #Novo texto
    despertador = "Você acorda com seu despertador tocando, olha para a janela, porém não vê luz do sol. Com toda essa poluição, é impossível velo de qualquer maneira. Mas você sabe olhando no relógio que já são 07:00am."
    inicio_narrador.config(text=despertador)

    #Novo botão
    botao.config(text="Ir para o banheiro", bg='#4682B4', fg='#ADD8E6', 
                font=('Space Mono', 9, 'italic'), command=banheiro)
    novo_botao = tk.Button(frame_inferior, text="Ver suas mensagens", bg='#4682B4', fg='#ADD8E6', 
                font=('Space Mono', 9, 'italic'))
    novo_botao.pack(pady=(0,20))

def banheiro():
    #Nova de fundo
    imagem = Image.open('img/Banheiro.jpg')
    nova_imagem = imagem.resize((720, 480))
    imagem_tk = ImageTk.PhotoImage(nova_imagem)
    label_imagem.config(image=imagem_tk)
    label_imagem.image = imagem_tk

    #Novo texto
    porta = "Você se levanta, meio tonto ainda da festa da noite passada, vai até o banheiro e enxuga a cara. Solta um barro e depois vai para a cozinha pegar algo para comer. \n\nEnquanto você está comendo escuta um barulho na porta. Alguém esta batendo."
    inicio_narrador.config(text=porta)

#Iniciar Aplicação
criar_interface()
janela.mainloop()
