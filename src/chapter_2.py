from tkinter import *
from estilo import limpar_frame, adicionar_texto, criar_botoes, imagem_de_fundo, janela, frame_rolavel
import tkinter as tk
from fichas import ficha_delacruz, atributos_movimento_delacruz
from saves import salvar_jogo, carregar_jogo , excluir_save

def alterar_imagem_de_fundo(frame, caminho_imagem):
    imagem_de_fundo(frame, caminho_imagem)

def inicio_Capitulo2(dados_jogo=None):
    limpar_frame(frame_rolavel)

    if dados_jogo:  # Se dados foram carregados
        texto_inicial = dados_jogo['texto_atual']
        imagem_fundo = dados_jogo['imagem_fundo']
        dinheiro = dados_jogo['DINHEIRO']
    else:
        # Dados padrão do início do capítulo
        imagem_fundo = 'img/Capitulo_2.jpg'
        dinheiro = 1500000
        texto_inicial = ("Você esta com sua parceira androide e seu cachorro robo Salsicha, vocês chegaram ao ponto de encontro que o Espinosa marcou, o Pinto Seco.")
        
    
    alterar_imagem_de_fundo(frame_rolavel, imagem_fundo)
    adicionar_texto(frame_rolavel, texto_inicial, row=1)
    adicionar_texto(frame_rolavel, f"Vocês não sabem qual missão ele irá oferecer para vocês, a unica informação é o pagamento, R$ {dinheiro:.2f}", fonte_tamanho=11, cor_texto='#00FF00', row=2)

    adicionar_texto(frame_rolavel, "-----------------------------------------------------------------------------------------------------------", fonte_tamanho=11, cor_texto='black', row=3)

    #Botão
    opcoes = [
            {'texto': "Ficha do Delacruz", 'comando': ficha_delacruz},
            {'texto': "Descer do Carro", 'comando': Entrada},
            {'texto': "Salvar Jogo", 'comando': lambda: salvar_jogo(atributos_movimento_delacruz, 'inicio_Capitulo2', texto_inicial, imagem_fundo), 'fg':'black', 'bg':'#009900'},  
            {'texto': "Carregar Jogo", 'comando': lambda: carregar_jogo(atributos_movimento_delacruz), 'fg':'black', 'bg':'#004d99'},
            {'texto': "Excluir Save", 'comando': excluir_save, 'fg':'black', 'bg':'#ff0000'}
    ]

    linha_inicial = 4
    criar_botoes(opcoes, linha_inicial)

def Entrada():
    #Nova de fundo
    limpar_frame(frame_rolavel)


    alterar_imagem_de_fundo(frame_rolavel, 'img/Entrada_Bar.jpg')

    texto_inicial = ("À sua frente, há várias mesas de madeira, dispostas sob toldos velhos e desgastados."
                     "\nAcima delas, um letreiro que já teve dias melhores exibe o nome 'Pinto Seco'. A entrada "
                     "está logo à frente, mas você precisará se esgueirar entre as mesas para chegar até a"
                     "porta. O bar está lotado."
                     "\n\nVocê se vira para sua parceira antes de entrar e percebe que ela está terminando de"
                     "vestir um sobretudo, cobrindo todo o corpo e levantando a gola até acima da boca.")
    adicionar_texto(frame_rolavel, texto_inicial, row=1)

    adicionar_texto(frame_rolavel, "-----------------------------------------------------------------------------------------------------------", fonte_tamanho=11, cor_texto='black', row=2)

    #Botão
    opcoes = [
            {'texto': "Questionar", 'comando': Preconceito_Androide},
            {'texto': "Entrar", 'comando': Bar}
    ]
    linha_inicial = 3
    criar_botoes(opcoes, linha_inicial)

def Preconceito_Androide():
    #Nova de fundo
    limpar_frame(frame_rolavel)

    alterar_imagem_de_fundo(frame_rolavel, 'img/Entrada_Bar.jpg')

    adicionar_texto(frame_rolavel, "'Paparazzi de mais por aqui?'", fonte_tamanho=11, cor_texto='#4682B4', row=1)

    adicionar_texto(frame_rolavel, "'Você sabe que androides são tão indesejados nesses lugares quanto ratos.'", fonte_tamanho=11, cor_texto='#d9ade6', row=2)

    adicionar_texto(frame_rolavel, "'Achava que com uma repórter de renome a hospitalidade seria diferente'", fonte_tamanho=11, cor_texto='#4682B4', row=3)

    adicionar_texto(frame_rolavel, "'Não em todo lugar, e muito menos em lugares com álcool.'", fonte_tamanho=11, cor_texto='#d9ade6', row=4)

    adicionar_texto(frame_rolavel, "'Vamos entrar, estão nos esperando'", fonte_tamanho=11, cor_texto='#d9ade6', row=5)

    adicionar_texto(frame_rolavel, "-----------------------------------------------------------------------------------------------------------", fonte_tamanho=11, cor_texto='black', row=6)

    #Botão
    opcoes = [
            {'texto': "Entrar", 'comando': Bar}
    ]
    linha_inicial = 7
    criar_botoes(opcoes, linha_inicial)

def Bar():
    #Nova de fundo
    limpar_frame(frame_rolavel)

    alterar_imagem_de_fundo(frame_rolavel, 'img/Bar.jpeg')

    texto_inicial = ("Vocês caminham até o fundo do bar, onde fica a área VIP. Pequenas salas quadradas, cada uma com "
                    "uma entrada de vidro fumê tão escuro quanto o céu à noite."
                    "\nEm frente a uma dessas salas, estão dois homens, cada um com quase dois metros de altura e braços "
                    "cibernéticos do tamanho de uma roda. Eles são os seguranças particulares de Espinosa."
                    "\n\nVocês se apresentam, e então eles abrem a porta. Dentro, há um sofá em formato de U e, à sua frente, uma mesa redonda."
                    "\nNo sofá, está sentado um senhor de aproximadamente 40 anos, com uma bengala apoiada no braço enquanto termina de gesticular algo."
                    "\nAo seu lado, há uma mulher jovem e bonita, vestindo um vestido vermelho claramente muito caro para o lugar em que se encontra."
                    "\nE, por fim, ao centro da mesa, está o Sr. Espinosa, um homem alto e esguio, com longos cabelos pretos. No lado direito do rosto, "
                    "ele tem um terceiro olho, além do braço esquerdo que é completamente cibernético."
                    "\n\nEle olha para vocês, faz um gesto com a mão para os seguranças saírem e diz:")
    adicionar_texto(frame_rolavel, texto_inicial, row=1)

    adicionar_texto(frame_rolavel, "'Sr. Delacruz e Srta. Rocha, estávamos aguardando a sua chegada. Sentem-se, podemos finalmente falar sobre negócios.'", fonte_tamanho=11, cor_texto='#b266b2', row=2)

    adicionar_texto(frame_rolavel, "-----------------------------------------------------------------------------------------------------------", fonte_tamanho=11, cor_texto='black', row=3)

    #Botão
    opcoes = [
            {'texto': "Missão", 'comando': Missao}
    ]
    linha_inicial = 4
    criar_botoes(opcoes, linha_inicial)

def Missao():
    #Nova de fundo
    limpar_frame(frame_rolavel)

    alterar_imagem_de_fundo(frame_rolavel, 'img/Bar.jpeg')

    adicionar_texto(frame_rolavel, "'Vou direto ao ponto. A empresa Cyberlife vai leiloar uma nova tecnologia, algo nunca antes visto na história humana." 
                    " Pelo menos é isso que os rumores têm contado.'", fonte_tamanho=11, cor_texto='#b266b2', row=1)

    adicionar_texto(frame_rolavel, "'Essa tecnologia será leiloada no leilão ilegal de androides, que acontecerá na mansão do atual diretor da Yoshida." 
                    " Neste sábado'", fonte_tamanho=11, cor_texto='#b266b2', row=2)

    adicionar_texto(frame_rolavel, "'O leilão será realizado no porão da mansão, enquanto, no andar de cima,"
                    " acontecerá uma festa em comemoração aos 85 anos da companhia.'", fonte_tamanho=11, cor_texto='#b266b2', row=3)

    adicionar_texto(frame_rolavel, "'Vocês entrarão no local como convidados da festa, mas para acessar o leilão precisarão utilizar suas..."
                    " habilidades. Alguma pergunta?'", fonte_tamanho=11, cor_texto='#b266b2', row=4)

    adicionar_texto(frame_rolavel, "\nSantiago Yamaha levanta a mão como se estivesse em uma sala de aula e diz:\n", fonte_tamanho=11, row=5)

    adicionar_texto(frame_rolavel, "'O cliente vai pagar 1.500.000 para roubarmos uma tecnologia que estará sendo LEILOADA?'", fonte_tamanho=11, cor_texto='#4bb446', row=6)

    adicionar_texto(frame_rolavel, "'Não seria mais fácil ele simplesmente... participar do leilão?'", fonte_tamanho=11, cor_texto='#4bb446', row=7)

    adicionar_texto(frame_rolavel, "\nEspinosa toma um gole do seu whisky que estava em cima da mesa.\n", fonte_tamanho=11, row=8)

    adicionar_texto(frame_rolavel, "'Os motivos para o nosso cliente nos contratar não nos interessam, mas posso garantir para vocês que, se essa tecnologia for tudo o que dizem,"
                    " um milhão seria apenas o valor inicial do leilão.'", fonte_tamanho=11, cor_texto='#b266b2', row=9)  

    adicionar_texto(frame_rolavel, "-----------------------------------------------------------------------------------------------------------", fonte_tamanho=11, cor_texto='black', row=10)

    #Botão
    opcoes = [
            {'texto': "Propor Revender a tecnologia", 'comando': Santiago_Roubo, 'fg':'black', 'bg':'#4bb446'},
            {'texto': "Perguntar de adiantamento", 'comando': Adiantamento,'fg':'black', 'bg':'#b4464b'}
    ]
    linha_inicial = 11
    criar_botoes(opcoes, linha_inicial)

def Santiago_Roubo():
    #Nova de fundo
    limpar_frame(frame_rolavel)

    alterar_imagem_de_fundo(frame_rolavel, 'img/Bar.jpeg')

    adicionar_texto(frame_rolavel, "'Então, por que vamos entregar o prêmio a ele?'", fonte_tamanho=11, cor_texto='#4bb446', row=1)

    adicionar_texto(frame_rolavel, "'Vamos ficar com a tecnologia e vender para quem pagar mais caro!'", fonte_tamanho=11, cor_texto='#4bb446', row=2)

    adicionar_texto(frame_rolavel, "'Primeiro, meus serviços não são requisitados por causa da minha cara bonita. Tenho princípios,"
                    " e eles incluem não passar a perna em um cliente.'", fonte_tamanho=11, cor_texto='#b266b2', row=3)

    adicionar_texto(frame_rolavel, "'Não... não quis dizer isso...'", fonte_tamanho=11, cor_texto='#4bb446', row=4)

    adicionar_texto(frame_rolavel, "\nSantiago tenta se corrigir, mas Espinosa o interrompe:\n", fonte_tamanho=11, row=5)

    adicionar_texto(frame_rolavel, "'Segundo! Mesmo que pudéssemos fazer isso, o item será leiloado não para pessoas comuns, mas para representantes das megacorporações."
                    " Somente megacorporações teriam dinheiro para pagar por esse produto.'", fonte_tamanho=11, cor_texto='#b266b2', row=6)

    adicionar_texto(frame_rolavel, "O que você acha que vai acontecer quando roubarmos empresas como a Cyberlife e a Yoshida, e uma semana depois esse produto aparecer à"
                    " venda no mercado negro? Quanto mais rápido nos livrarmos disso, melhor.'", fonte_tamanho=11, cor_texto='#b266b2', row=7)

    adicionar_texto(frame_rolavel, "\nSakura acrescenta:\n", fonte_tamanho=11, row=8)

    adicionar_texto(frame_rolavel, "'Não estou nesse negócio para favorecer nenhuma megacorporação, Santiago.'", fonte_tamanho=11, cor_texto='#b4464b', row=9)  

    adicionar_texto(frame_rolavel, "-----------------------------------------------------------------------------------------------------------", fonte_tamanho=11, cor_texto='black', row=10)

    #Botão
    opcoes = [
            {'texto': "Terminar conversa", 'comando': Finalizar_Instrucao}
    ]
    linha_inicial = 11
    criar_botoes(opcoes, linha_inicial)

def Adiantamento():
    #Nova de fundo
    limpar_frame(frame_rolavel)

    from fichas import atributos_movimento_delacruz

    alterar_imagem_de_fundo(frame_rolavel, 'img/Bar.jpeg')

    adicionar_texto(frame_rolavel, "'E quanto ao adiantamento, Espinosa?'", fonte_tamanho=11, cor_texto='#b4464b', row=1)

    adicionar_texto(frame_rolavel, "'Precisamos nos preparar bem antes da missão.'", fonte_tamanho=11, cor_texto='#b4464b', row=2)

    adicionar_texto(frame_rolavel, "'Claro, o adiantamento é de 10% do valor total. Como de costume, seguro o valor do adiantamento fornecido até o"
                    " final da missão, mas neste caso...'", fonte_tamanho=11, cor_texto='#b266b2', row=3)

    adicionar_texto(frame_rolavel, "\nEspinosa começa a teclar algumas coisas em seu braço cibernético e então conclui:\n", fonte_tamanho=11, row=4)

    adicionar_texto(frame_rolavel, "'Já foram depositados na conta de vocês R$2.000,00 para ajudar nas despesas iniciais.'", fonte_tamanho=11, cor_texto='#b266b2', row=5)

    adicionar_texto(frame_rolavel, "'O restante do pagamento será realizado pelo cliente após a conclusão da missão.'", fonte_tamanho=11, cor_texto='#b266b2', row=6)

    adicionar_texto(frame_rolavel, "-----------------------------------------------------------------------------------------------------------", fonte_tamanho=11, cor_texto='black', row=10)

    #Aumentar o valor de DINHEIRO
    atributos_movimento_delacruz['DINHEIRO'] += 2000

    #Botão
    opcoes = [
            {'texto': "Terminar conversa", 'comando': Finalizar_Instrucao}
    ]
    linha_inicial = 11
    criar_botoes(opcoes, linha_inicial)

def Finalizar_Instrucao():
    #Nova de fundo
    limpar_frame(frame_rolavel)

    alterar_imagem_de_fundo(frame_rolavel, 'img/Bar.jpeg')

    adicionar_texto(frame_rolavel, "'Pois bem, espero ter deixado tudo claro para vocês.'", fonte_tamanho=11, cor_texto='#b266b2', row=1)

    adicionar_texto(frame_rolavel, "'Estou encaminhando a planta do local junto com o telefone para me ligarem assim que a missão for concluída.'", fonte_tamanho=11, cor_texto='#b266b2', row=2)

    adicionar_texto(frame_rolavel, "'...Espero que entendam que não podemos falhar, ou todas as nossas cabeças estarão a prêmio.'", fonte_tamanho=11, cor_texto='#b266b2', row=3)

    adicionar_texto(frame_rolavel, "\nVocês quatro se levantam e saem do bar. Do lado de fora, decidem o que fazer.\n", fonte_tamanho=11, row=4)

    adicionar_texto(frame_rolavel, "'Minha oficina não fica muito longe daqui. Podemos ir para lá analisar melhor a planta.'", fonte_tamanho=11, cor_texto='#4bb446', row=5)

    adicionar_texto(frame_rolavel, "'Boa ideia, Santiago, mas só temos 2 dias para nos prepararmos. Acho que a prioridade é nos abastecermos primeiro.'", fonte_tamanho=11, cor_texto='#d9ade6', row=6)

    adicionar_texto(frame_rolavel, "-----------------------------------------------------------------------------------------------------------", fonte_tamanho=11, cor_texto='black', row=7)

    #Botão
    opcoes = [
            {'texto': "Ficha de Santiago Yamaha", 'comando': None, 'fg':'black', 'bg':'#4bb446'},
            {'texto': "Ficha de Isabela Rocha", 'comando': None, 'fg':'black', 'bg':'#4bb446'},
            {'texto': "Ficha de Sakura Sato", 'comando': None, 'fg':'black', 'bg':'#4bb446'},

            {'texto': "Planejar missão", 'comando': None, 'fg':'black', 'bg':'#4bb446'},
            {'texto': "Reabastecer", 'comando': None, 'fg':'black', 'bg':'#d9ade6'}
    ]
    linha_inicial = 8
    criar_botoes(opcoes, linha_inicial)


inicio_Capitulo2()


# Delacruz #4682B4
# Yamaha #4bb446
# Sakura #b4464b
# Rocha #d9ade6
# Espinosa #b266b2