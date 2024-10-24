import json
import os

def salvar_jogo(atributos_movimento_delacruz, capitulo_atual, texto_atual, imagem_fundo):
    estado_jogo = {
        "capitulo_atual": capitulo_atual,
        "dados_jogo": {
            "VIT": atributos_movimento_delacruz['VIT'],
            "DINHEIRO": atributos_movimento_delacruz['DINHEIRO'],
            "texto_atual": texto_atual,
            "imagem_fundo": imagem_fundo 
        }
    }
    
    with open('jogo_save.json', 'w') as f:
        json.dump(estado_jogo, f)
    print("Jogo salvo com sucesso!")

def carregar_jogo(atributos_movimento_delacruz):
    from chapter_2 import inicio_Capitulo2
    try:
        with open('jogo_save.json', 'r') as f:
            estado = json.load(f)

        atributos_movimento_delacruz['VIT'] = estado['dados_jogo']['VIT']
        atributos_movimento_delacruz['DINHEIRO'] = estado['dados_jogo']['DINHEIRO']
        
        # Chama o capítulo salvo
        capitulo_atual = estado['capitulo_atual']
        
        if capitulo_atual == "inicio_Capitulo2":
            inicio_Capitulo2(estado['dados_jogo'])  # Passa os dados do jogo
        # Adicione outros capítulos aqui conforme necessário

        print("Jogo carregado com sucesso!")
    except FileNotFoundError:
        print("Arquivo de save não encontrado.")

def excluir_save():
    try:
        os.remove('jogo_save.json')
        print("Arquivo de save excluído com sucesso!")
    except FileNotFoundError:
        print("Arquivo de save não encontrado.")