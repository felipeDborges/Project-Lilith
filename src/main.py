from tkinter import *
from estilo import limpar_frame, adicionar_texto, criar_botoes, imagem_de_fundo, janela, frame_rolavel
import tkinter as tk
from chapter_2 import *

bloquearSantiago = False
cameraCasa = False

def alterar_imagem_de_fundo(frame, caminho_imagem):
    imagem_de_fundo(frame, caminho_imagem)

def inicio():
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
    opcoes = [
            {'texto': "Acordar", 'comando': despertar},
            {'texto': "Carregar Jogo", 'comando': lambda: carregar_jogo(atributos_movimento_delacruz)},
            {'texto': "Excluir Save", 'comando': excluir_save, 'fg':'black', 'bg':'red'}
    ]
    linha_inicial = 2
    criar_botoes(opcoes, linha_inicial)

def despertar():
    # Limpar o frame rolável
    limpar_frame(frame_rolavel)

    #Nova de fundo
    alterar_imagem_de_fundo(frame_rolavel, 'img/Quarto.jpg')

    #Novo texto
    despertador = "Você acorda com seu despertador tocando, olha para a janela, porém não vê luz do sol. Com toda essa poluição, é impossível velo de qualquer maneira. Mas você sabe olhando no relógio que já são 07:00am."
    adicionar_texto(frame_rolavel, despertador, row=1)

    opcoes = [
        {'texto': "Ir para o banheiro", 'comando': banheiro},
        {'texto': "Ver suas mensagens", 'comando': mensagens}
    ]

    linha_inicial = 2

    criar_botoes(opcoes, linha_inicial)

def banheiro():
    # Limpar o frame rolável
    limpar_frame(frame_rolavel)

    #Nova de fundo
    alterar_imagem_de_fundo(frame_rolavel, 'img/Banheiro.jpg')

    #Novo texto
    porta = ("Você se levanta, meio tonto ainda da festa da noite passada, vai até o banheiro e enxuga a cara. "
             "Solta um barro e depois vai para a cozinha pegar algo para comer. \n\nEnquanto você está comendo, "
             "escuta um barulho na porta.")
    adicionar_texto(frame_rolavel, porta, row=1)
    adicionar_texto(frame_rolavel, "Alguém está batendo.", fonte_tamanho=11, cor_texto='#e6bcad', row=2)

    #Novo botão
    opcoes = [
        {'texto': "Olhar nas câmeras", 'comando': camera},
        {'texto': "Abrir a porta", 'comando': abrir_a_porta},
        {'texto': "Ignorar", 'comando': ignorar}
    ]
    linha_inicial = 3

    criar_botoes(opcoes, linha_inicial)

def mensagens():
    # Limpar o frame rolável
    limpar_frame(frame_rolavel)

    #Nova de fundo
    alterar_imagem_de_fundo(frame_rolavel, 'img/Quarto.jpg')

    #Novo texto
    mensagem1 = ("Você possui um celular físico, prefere isso a ficar recebendo propagandas neurais em sua cabeça toda hora.")
    adicionar_texto(frame_rolavel, mensagem1, row=1)

    mensagem2 = ("Ao abrir suas notificações, você vê 45 mensagens não lidas do Santiago Yamaha, todas elas com a mensagem:")
    adicionar_texto(frame_rolavel, mensagem2, row=2)

    mensagem3 = ("VAMOS FICAR RICOS PORRA! \n\n... repetidas várias vezes.")
    adicionar_texto(frame_rolavel, mensagem3, row=3)

    #Novo botão
    opcoes = [
        {'texto': "Ver mensagens de Sakura", 'comando': mensagens_sakura},
        {'texto': "Ver mensagens de Espinosa", 'comando': mensagens_espinoas},
        {'texto': "Bloquear Santiago", 'comando': bloquear_santiago},
        {'texto': "Levantar", 'comando': banheiro}
    ]
    linha_inicial = 4

    criar_botoes(opcoes, linha_inicial)

def bloquear_santiago():
    global bloquearSantiago

    # Limpar o frame rolável
    limpar_frame(frame_rolavel)

    #Nova de fundo
    alterar_imagem_de_fundo(frame_rolavel, 'img/Quarto.jpg')

    #Novo texto
    mensagem1 = ("Você bloqueia Santiago.")
    adicionar_texto(frame_rolavel, mensagem1, row=1)

    adicionar_texto(frame_rolavel, "-----------------------------------------------------------------------------------------------------------", fonte_tamanho=11, cor_texto='black', row=2)

    bloquearSantiago = True

    #Novo botão
    opcoes = [
        {'texto': "Ver mensagens de Sakura", 'comando': mensagens_sakura},
        {'texto': "Ver mensagens de Espinosa", 'comando': mensagens_espinoas},
        {'texto': "Levantar", 'comando': banheiro}
    ]
    linha_inicial = 3

    criar_botoes(opcoes, linha_inicial)

def mensagens_sakura():
    # Limpar o frame rolável
    limpar_frame(frame_rolavel)

    #Nova de fundo
    alterar_imagem_de_fundo(frame_rolavel, 'img/Quarto.jpg')

    #Novo texto
    mensagem1 = ("Espinosa nunca falou o valor do pagamento antes de explicar o trabalho..")
    adicionar_texto(frame_rolavel, mensagem1, row=1)

    mensagem2 = ("Ele REALMENTE esta desesperado")
    adicionar_texto(frame_rolavel, mensagem2, row=2)

    adicionar_texto(frame_rolavel, "-----------------------------------------------------------------------------------------------------------", fonte_tamanho=11, cor_texto='black', row=3)

    if bloquearSantiago == False:
        opcoes = [
            {'texto': "Ver mensagens de Espinosa", 'comando': mensagens_espinoas},
            {'texto': "Bloquear Santiago", 'comando': bloquear_santiago},
            {'texto': "Levantar", 'comando': banheiro}
        ]
    else:
        opcoes = [
            {'texto': "Ver mensagens de Espinosa", 'comando': mensagens_espinoas},
            {'texto': "Levantar", 'comando': banheiro}
        ]
    linha_inicial = 4

    criar_botoes(opcoes, linha_inicial)

def mensagens_espinoas():
    # Limpar o frame rolável
    limpar_frame(frame_rolavel)

    #Nova de fundo
    alterar_imagem_de_fundo(frame_rolavel, 'img/Quarto.jpg')

    #Novo texto
    mensagem1 = ("Como definido, 08am no Pinto Seco.")
    adicionar_texto(frame_rolavel, mensagem1, row=1)

    adicionar_texto(frame_rolavel, "NÃO SE ATRASE", fonte_tamanho=15, cor_texto='red', row=2)

    adicionar_texto(frame_rolavel, "-----------------------------------------------------------------------------------------------------------", fonte_tamanho=11, cor_texto='black', row=3)

    if bloquearSantiago == False:
        opcoes = [
            {'texto': "Ver mensagens de Sakura", 'comando': mensagens_sakura},
            {'texto': "Bloquear Santiago", 'comando': bloquear_santiago},
            {'texto': "Levantar", 'comando': banheiro}
        ]
    else:
        opcoes = [
            {'texto': "Ver mensagens de Sakura", 'comando': mensagens_sakura},
            {'texto': "Levantar", 'comando': banheiro}
        ]
    linha_inicial = 4

    criar_botoes(opcoes, linha_inicial)

def camera():
    global cameraCasa
    # Limpar o frame rolável
    limpar_frame(frame_rolavel)

    #Nova de fundo
    alterar_imagem_de_fundo(frame_rolavel, 'img/Cozinha.jpg')

    #Novo texto
    porta = ("Você pega sua braçadeira que tinha largado em cima da mesa. Ela é robusta parecendo uma braçadeira medieval, em sua parte de cima tem um visor de LED onde você controla boa parte das coisas."
             "Você abre as câmeras de segurança e verifica quem está do outro lado da porta."
             "Uma mulher, com cabelos azuis neon e uma roupa discreta e amarrotada."
             "Não precisa de muito esforço para saber que essa pele é sintética, com linhas marcando as partes onde termina uma pele e começa outra." 
             "É um androide, você odeia androides, mas essa em específico você consegue aturar... As vezes. ")
    adicionar_texto(frame_rolavel, porta, row=1)

    cameraCasa = True

    opcoes = [
            {'texto': "Atender a porta", 'comando': abrir_a_porta_camera},
            {'texto': "Ignorar", 'comando': ignorar}
    ]
    linha_inicial = 2

    criar_botoes(opcoes, linha_inicial)

def abrir_a_porta ():
    # Limpar o frame rolável
    limpar_frame(frame_rolavel)

    #Nova de fundo
    alterar_imagem_de_fundo(frame_rolavel, 'img/Cozinha.jpg')

    #Novo texto
    mensagem1 = ("Ao abrir a porta você se depara com uma mulher, com cabelos azuis neon e uma roupa discreta e amarrotada. "
             "Não precisa de muito esforço para saber que essa pele é sintética, com linhas marcando as partes onde termina uma pele e começa outra. "
             "É uma androide, você odeia androides mas essa em específico você consegue aturar... As vezes.")
    adicionar_texto(frame_rolavel, mensagem1, row=1)

    mensagem2 = ("Ela olha para você e diz:")
    adicionar_texto(frame_rolavel, mensagem2, row=2)

    adicionar_texto(frame_rolavel, "'Achei que nunca iria atender.'", fonte_tamanho=11, cor_texto='#d9ade6', row=3)

    adicionar_texto(frame_rolavel, "'Eu estava ocupando, tomando meu café da manhã'", fonte_tamanho=11, cor_texto='#4682B4', row=4)

    adicionar_texto(frame_rolavel, "'Eu ouvi, já ta pronto?'", fonte_tamanho=11, cor_texto='#d9ade6', row=5)

    adicionar_texto(frame_rolavel, "'Só preciso pegar o Salsicha e já to saindo'", fonte_tamanho=11, cor_texto='#4682B4', row=6)

    mensagem3 = ("Você pega sua braçadeira que tinha largado em cima da mesa. Ela é robusta parecendo uma braçadeira medieval, " 
                 "em sua parte de cima tem um visor de LED onde você controla boa parte das coisas. "
             "Após prender no braço você pelo visor tira do modo stund-by seu cachorro robótico, você escuta os engrenagens dele ligando. " 
             "Ele sai da sua base recarregavel e vem até você soltando um latido sintetico. ")
    adicionar_texto(frame_rolavel, mensagem3, row=7)

    adicionar_texto(frame_rolavel, "'Pronto, podemos ir agora'", fonte_tamanho=11, cor_texto='#4682B4', row=8)

    opcoes = [
            {'texto': "Ir para fora", 'comando': saindo}
    ]
    linha_inicial = 9

    criar_botoes(opcoes, linha_inicial)

def ignorar():
    # Limpar o frame rolável
    limpar_frame(frame_rolavel)

    #Nova de fundo
    alterar_imagem_de_fundo(frame_rolavel, 'img/Cozinha.jpg')

    #Novo texto
    mensagem1 = ("Você continua comento seu serial matinal e ignora as batidas da porta. "
                "Elas então ficam mais fortes e você escuta uma voz vindo de fora: ")
    adicionar_texto(frame_rolavel, mensagem1, row=1)

    adicionar_texto(frame_rolavel, "'Bruno! Eu sei que você está aí dentro, vamos logo que não quero me atrasar.'", fonte_tamanho=11, cor_texto='#d9ade6', row=2)

    mensagem2 = ("A voz é feminina, porém levemente robotizada. Como se estivesse saindo de uma caixa de som.")
    adicionar_texto(frame_rolavel, mensagem2, row=3)

    if cameraCasa == False:
        opcoes = [
            {'texto': "Masticar meu serial matinal", 'comando': ignorar_mais},
            {'texto': "Abrir a porta", 'comando': abrir_a_porta},
            {'texto': "Olhar nas câmeras", 'comando': camera},
        ]
    else:
        opcoes = [
            {'texto': "Masticar meu serial matinal", 'comando': ignorar_mais},
            {'texto': "Abrir a porta", 'comando': abrir_a_porta_camera}
        ]
    linha_inicial = 4

    criar_botoes(opcoes, linha_inicial)

def ignorar_mais():
    # Limpar o frame rolável
    limpar_frame(frame_rolavel)

    #Nova de fundo
    alterar_imagem_de_fundo(frame_rolavel, 'img/Cozinha.jpg')

    #Novo texto
    mensagem1 = ("Você continua mastigando seu serial matinal, mais e mais ignorando o barulho na porta.")
    adicionar_texto(frame_rolavel, mensagem1, row=1)

    adicionar_texto(frame_rolavel, "'Eu ''LITERALMENTE'' consigo ouvir você mastigar essa porcaria de serial cheio de conservantes, dá para atender?' ", fonte_tamanho=11, cor_texto='#d9ade6', row=2)

    if cameraCasa == False:
        opcoes = [
            {'texto': "Mastigar MAIS ALTO serial matinal", 'comando': ignorar_mais_maisForte},
            {'texto': "Abrir a porta", 'comando': abrir_a_porta},
            {'texto': "Olhar nas câmeras", 'comando': camera},
    ]
    else:
        opcoes = [
            {'texto': "Mastigar MAIS ALTO serial matinal", 'comando': ignorar_mais_maisForte},
            {'texto': "Abrir a porta", 'comando': abrir_a_porta_camera}
    ]
    linha_inicial = 3

    criar_botoes(opcoes, linha_inicial)

def ignorar_mais_maisForte():
    # Limpar o frame rolável
    limpar_frame(frame_rolavel)

    #Nova de fundo
    alterar_imagem_de_fundo(frame_rolavel, 'img/Cozinha.jpg')

    #Novo texto
    mensagem1 = ("Você começa a fazer barulhos cada vez mais altos enquanto come seu serial, e diz: ")
    adicionar_texto(frame_rolavel, mensagem1, row=1)

    adicionar_texto(frame_rolavel, "'Você sabe que ODEIO quando fica fuxicando o que to fazendo!'", fonte_tamanho=11, cor_texto='#4682B4', row=2)

    adicionar_texto(frame_rolavel, "'É só abrir essa porta que eu paro, e vê se fecha sua torneira! A água do mundo ta acabando, esqueceu!'", fonte_tamanho=11, cor_texto='#d9ade6',row=3)

    mensagem2 = ("Você olha para a pia do banheiro e vê que deixou a torneira pingando")
    adicionar_texto(frame_rolavel, mensagem2, row=4)

    if cameraCasa == False:
        opcoes = [
            {'texto': "Ir comer no banheiro", 'comando': ignorando_supremo},
            {'texto': "Abrir a porta", 'comando': abrir_a_porta},
            {'texto': "Olhar nas câmeras", 'comando': camera},
    ]
    else:
        opcoes = [
            {'texto': "Ir comer no banheiro", 'comando': ignorando_supremo},
            {'texto': "Abrir a porta", 'comando': abrir_a_porta_camera}
    ]
    linha_inicial = 5

    criar_botoes(opcoes, linha_inicial)

def ignorando_supremo():
    # Limpar o frame rolável
    limpar_frame(frame_rolavel)

    #Nova de fundo
    alterar_imagem_de_fundo(frame_rolavel, 'img/Banheiro.jpg')

    #Novo texto
    mensagem1 = ("Você senta na privada e continua comendo seu serial matinal.")
    adicionar_texto(frame_rolavel, mensagem1, row=1)

    mensagem2 = ("Você ainda continua ouvindo a porta batendo.")
    adicionar_texto(frame_rolavel, mensagem2, row=2)

    adicionar_texto(frame_rolavel, "-----------------------------------------------------------------------------------------------------------", fonte_tamanho=11, cor_texto='black', row=3)

    if cameraCasa == False:
        opcoes = [
            {'texto': "Abrir a porta", 'comando': abrir_a_porta},
            {'texto': "Olhar nas câmeras", 'comando': camera},
    ]
    else:
        opcoes = [
            {'texto': "Abrir a porta", 'comando': abrir_a_porta_camera}
    ]
    linha_inicial = 4

    criar_botoes(opcoes, linha_inicial)

def abrir_a_porta_camera(): 
    # Limpar o frame rolável
    limpar_frame(frame_rolavel)

    #Nova de fundo
    alterar_imagem_de_fundo(frame_rolavel, 'img/Cozinha.jpg')

    #Novo texto
    mensagem1 = ("Ao abrir a porta você se depara com a mulher da câmera. \n \n Ela olha para você e diz: ")
    adicionar_texto(frame_rolavel, mensagem1, row=1)

    adicionar_texto(frame_rolavel, "'Achei que nunca iria atender.'", fonte_tamanho=11, cor_texto='#d9ade6', row=2)

    adicionar_texto(frame_rolavel, "'Eu estava ocupando, tomando meu café da manhã'", fonte_tamanho=11, cor_texto='#4682B4', row=3)

    adicionar_texto(frame_rolavel, "'Eu ouvi, já ta pronto?'", fonte_tamanho=11, cor_texto='#d9ade6', row=4)

    adicionar_texto(frame_rolavel, "'Só preciso pegar o Salsicha e já to saindo'", fonte_tamanho=11, cor_texto='#4682B4', row=5)

    mensagem3 = ("Você olha para seu braço, a onde agora esta sua braçadeira e então pelo visor tira do modo stund-by seu cachorro robótico, você escuta os engrenagens dele ligando." 
                 "Ele sai da sua base recarregavel e vem até você soltando um latido sintetico. ")
    adicionar_texto(frame_rolavel, mensagem3, row=6)

    adicionar_texto(frame_rolavel, "'Pronto, podemos ir agora'", fonte_tamanho=11, cor_texto='#4682B4', row=7)

    opcoes = [
            {'texto': "Ir para fora", 'comando': saindo}
    ]
    linha_inicial = 8

    criar_botoes(opcoes, linha_inicial)

def saindo ():
    # Limpar o frame rolável
    limpar_frame(frame_rolavel)

    #Nova de fundo
    alterar_imagem_de_fundo(frame_rolavel, 'img/Lojas.jpg')

    #Novo texto
    mensagem1 = ("Vocês pegam o levador do seu apartamento, descem mais de 32 andares até chegar no terrio, após isso ainda precisa passar por alguns comerciantes da zona de comercio do agrumerado de prédios, dessa megatorre que você vive.")
    adicionar_texto(frame_rolavel, mensagem1, row=1)

    mensagem2 = ("Ao sair dessa zona vocês chagam em fim na rua, a onde o carro de sua parceira esta estacionado. Uma linha de carros vintage da Chevrolet, um 'Chevrolet 1951', ela gosta dessa estetica de dois seculos atrás.")
    adicionar_texto(frame_rolavel, mensagem2, row=2)

    mensagem3 = ("Ela entra no carro e vc a acompanha para o banco de passageiro, a parte de cima do carro se abre, virando um conversivel, seu cachorro pula para o banco de trás. Ela liga o motor e voua com o carro para o engarrafamento aerio de São Paulo.")
    adicionar_texto(frame_rolavel, mensagem3, row=3)

    opcoes = [
            {'texto': "Perguntar a onde fica Pinto Seco", 'comando': localizacao},
            {'texto': "Falar sobre a missão", 'comando': papo_furado},
            {'texto': "Ler Jornal", 'comando': jornal_dia_1},
    ]
    linha_inicial = 4

    criar_botoes(opcoes, linha_inicial)

def localizacao ():
    # Limpar o frame rolável
    limpar_frame(frame_rolavel)

    #Nova de fundo
    alterar_imagem_de_fundo(frame_rolavel, 'img/Lojas.jpg')

    #Novo texto
    adicionar_texto(frame_rolavel, "'Então, esse tal de Pinto Seco é novo. Sabe onde fica?'", fonte_tamanho=11, cor_texto='#4682B4', row=1)

    adicionar_texto(frame_rolavel, "'Osasco'", fonte_tamanho=11, cor_texto='#d9ade6', row=2)

    adicionar_texto(frame_rolavel, "'Na parte baixa?'", fonte_tamanho=11, cor_texto='#4682B4', row=3)

    adicionar_texto(frame_rolavel, "'Sim'", fonte_tamanho=11, cor_texto='#d9ade6', row=4)

    adicionar_texto(frame_rolavel, "'...Saquei...' ", fonte_tamanho=11, cor_texto='#4682B4', row=5)

    adicionar_texto(frame_rolavel, "'Algum problema com a cidade?'", fonte_tamanho=11, cor_texto='#d9ade6', row=6)

    adicionar_texto(frame_rolavel, "'Policiais não são muito bem-vistos naquela região, e eu também não gosto dos tipos de pessoas que passam lá'", fonte_tamanho=11, cor_texto='#4682B4', row=7)   

    adicionar_texto(frame_rolavel, "'Disse o mercenário haha'", fonte_tamanho=11, cor_texto='#d9ade6', row=8)

    opcoes = [
            {'texto': "Falar sobre a missão", 'comando': papo_furado},
            {'texto': "Ler Jornal", 'comando': jornal_dia_1},
    ]
    linha_inicial = 9

    criar_botoes(opcoes, linha_inicial)

def papo_furado ():
    # Limpar o frame rolável
    limpar_frame(frame_rolavel)

    #Nova de fundo
    alterar_imagem_de_fundo(frame_rolavel, 'img/Trafego_Aereo.jpg')

    #Novo texto
    adicionar_texto(frame_rolavel, "'Tem alguma ideia do que pode ser essa missão?'", fonte_tamanho=11, cor_texto='#4682B4', row=1)

    adicionar_texto(frame_rolavel, "'Para o Espinosa já ter falado o valor? Não sei, matar alguma politico talvez?'", fonte_tamanho=11, cor_texto='#d9ade6', row=2)

    adicionar_texto(frame_rolavel, "'...O cliente pagar 1.500.000 Reais é algo sureal, vai ser nosso maior trabalho.'", fonte_tamanho=11, cor_texto='#4682B4', row=3)

    adicionar_texto(frame_rolavel, "'Nervoso?'", fonte_tamanho=11, cor_texto='#d9ade6', row=4)

    adicionar_texto(frame_rolavel, "'Não, só espero não ter que usar metade da minha parte para fugir do pais.'", fonte_tamanho=11, cor_texto='#4682B4', row=5)

    adicionar_texto(frame_rolavel, "-----------------------------------------------------------------------------------------------------------", fonte_tamanho=11, cor_texto='black', row=6)

    opcoes = [
            {'texto': "Perguntar a onde fica Pinto Seco", 'comando': localizacao},
            {'texto': "Ler Jornal", 'comando': jornal_dia_1},
    ]
    linha_inicial = 7

    criar_botoes(opcoes, linha_inicial)

def jornal_dia_1 ():
    # Limpar o frame rolável
    limpar_frame(frame_rolavel)

    #Nova de fundo
    alterar_imagem_de_fundo(frame_rolavel, 'img/Trafego_Aereo.jpg')

    #Novo texto
    adicionar_texto(frame_rolavel, "Quinta-feira, 17 de abril de 2121", fonte_tamanho=13, cor_texto='#ade6da', row=1)

    adicionar_texto(frame_rolavel, "Crise Hídrica Agrava Situação em SP", fonte_tamanho=12, cor_texto='#ade6da', row=2)

    adicionar_texto(frame_rolavel, "África sofre nova invasão pela Austrália; impactos globais são iminentes", fonte_tamanho=12, cor_texto='#ade6da', row=3)

    mensagem2 = ("O governo australiano lançou uma nova ofensiva militar em território africano, intensificando o conflito em busca de recursos naturais." 
                 "Enquanto isso, a crise de água atinge um novo pico no Brasil, com o estado de São Paulo enfrentando um novo fechamento total dos registros neste fim de semana." 
                 "As medidas visam preservar os escassos recursos hídricos, agravando a já tensa situação social e econômica na região.")
    adicionar_texto(frame_rolavel, mensagem2, row=4)

    opcoes = [
            {'texto': "Fim do Capítulo", 'comando': inicio_Capitulo2},
    ]
    linha_inicial = 5

    criar_botoes(opcoes, linha_inicial)

#Iniciar Aplicação
inicio()
janela.mainloop()
