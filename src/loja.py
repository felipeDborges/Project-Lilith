from tkinter import *
from estilo import limpar_frame, adicionar_texto, janela, frame_rolavel
from inventario import adicionar_item, exibir_inventario  # Importa o inventário e a função de exibição
from fichas import atributos_movimento_delacruz

# Itens disponíveis na loja
itens_loja = {
    "Espada": 875,
    "Escudo": 1000,
    "Poção de Vida": 850,
    "Armadura Leve": 500,
    "Bomba de Fumaça": 50
}

def abrir_inventario():
    """Chama a função para exibir o inventário.""" 
    exibir_inventario()  # Chama a função de exibição do inventário

def comprar_item(item):
    preco = itens_loja[item]
    
    if atributos_movimento_delacruz['DINHEIRO'] >= preco:
        atributos_movimento_delacruz['DINHEIRO'] -= preco
        adicionar_item(item)  # Adiciona o item ao inventário
        adicionar_texto(frame_rolavel, f"Você comprou {item} por {preco} moedas.", cor_texto='green', row=22)
    else:
        adicionar_texto(frame_rolavel, "Não há dinheiro suficiente.", cor_texto='red', row=22)

def criar_loja():
    # Limpa o frame atual antes de criar a loja
    limpar_frame(frame_rolavel)  # Certifique-se de que você tem essa função no seu estilo
    row = 0

    for item, preco in itens_loja.items():
        botao_item = Button(frame_rolavel, text=f"{item} - {preco} moedas", command=lambda i=item: comprar_item(i), bg='#4682B4', fg='#ADD8E6')
        botao_item.grid(row=row, column=0, padx=5, pady=5)
        row += 1
    
    # Botão para abrir o inventário
    botao_inventario = Button(frame_rolavel, text="Ver Inventário", command=abrir_inventario, bg='#4682B4', fg='#ADD8E6')
    botao_inventario.grid(row=row, column=0, padx=5, pady=5)  # Usando grid() em vez de pack()

    row += 1  # Incrementa a linha para o próximo botão

    # Botão para voltar ao menu principal ou fechar a loja
    botao_fechar = Button(frame_rolavel, text="Fechar Loja", command=lambda: limpar_frame(frame_rolavel), bg='#FF4500', fg='white')
    botao_fechar.grid(row=row, column=0, padx=5, pady=5)  # Usando grid() em vez de pack()

# Chama a função para criar a loja
criar_loja()

janela.mainloop()
