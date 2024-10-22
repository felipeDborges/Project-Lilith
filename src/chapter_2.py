from tkinter import *
from estilo import limpar_frame, adicionar_texto, criar_botoes, imagem_de_fundo, janela, frame_rolavel
import tkinter as tk
from fichas import *

def alterar_imagem_de_fundo(frame, caminho_imagem):
    imagem_de_fundo(frame, caminho_imagem)

def inicio_Capitulo2():
    #Nova de fundo
    limpar_frame(frame_rolavel)

    alterar_imagem_de_fundo(frame_rolavel, 'img/Capitulo_2.jpg')

    texto_inicial = ("Você esta com sua parceira androide e seu cachorro robo Salsicha, vocês chegaram ao ponto de encontro que o Espinosa marcou, o Pinto Seco. "
                     "Vocês não sabem qual missão ele irá oferecer para vocês, a unica informação é o pagamento,")
    adicionar_texto(frame_rolavel, texto_inicial, row=1)
    adicionar_texto(frame_rolavel, "R$ 1.500.000,00", fonte_tamanho=11, cor_texto='#00FF00', row=1)

    #Botão
    opcoes = [
            {'texto': "Ficha do Delacruz", 'comando': ficha_delacruz},
            {'texto': "Descer do Carro", 'comando': Entrada}
    ]

    linha_inicial = 1
    criar_botoes(opcoes, linha_inicial)

def Entrada():
    #Nova de fundo
    limpar_frame(frame_rolavel)


    alterar_imagem_de_fundo(frame_rolavel, 'img/Inicio_Sonho.jpg')

    texto_inicial = ("Estamos no distante e distópico futuro de 2121, após os acontecimentos da Terceira Grande Guerra, "
                     "o Brasil foi um dos poucos países que não sofreram ataques devastadores em seu território. "
                     "Assim, o Novo México e os poucos remanescentes do Japão se uniram ao Brasil levando sua cultura "
                     "e conhecimento à grande nação. Agora, o Brasil lidera o mundo em suas pesquisas de aperfeiçoamento humano. "
                     "\nUma dessas pesquisas se chama “Projeto Lilith”, uma arma nunca antes imaginada, que nossos "
                     "protagonistas foram contratados para roubá-la, porém o que eles não esperavam era que essa simples missão "
                     "se tornaria o estopim para o possível fim do mundo.")
    adicionar_texto(frame_rolavel, texto_inicial, row=1)

    #Botão
    botao_inicial = tk.Button(frame_rolavel, text="Acordar", bg='#4682B4', fg='#ADD8E6', 
                font=('Space Mono', 9, 'italic'), command=Entrada)
    botao_inicial.grid(row=2, column=0, padx=10, pady=10)


inicio_Capitulo2()

