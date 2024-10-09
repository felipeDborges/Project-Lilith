import tkinter as tk


def texto_narrador(janela, texto, wraplength, cor_fundo, cor_texto, fonte_tamanho):
    fonte = ('Space Mono', fonte_tamanho, 'italic')
    rotulo = tk.Label(janela, text=texto, wraplength=wraplength, bg=cor_fundo, fg=cor_texto, font=fonte)
    return rotulo


def texto_conversa(janela, texto, wraplength, cor_fundo, cor_texto, fonte_tamanho):
    fonte = ('Space Mono', fonte_tamanho)
    rotulo = tk.Label(janela, text=texto, wraplength=wraplength, bg=cor_fundo, fg=cor_texto, font=fonte)
    return rotulo