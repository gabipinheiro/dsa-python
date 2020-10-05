# Roletrando
# Sorteio de palavras por tipo

# Import
from ROLETRANDO.dicionario_palavras import dict_palavras
import random

#Sorteio de palavras
def sorteio():
    dicionario = dict_palavras()

    # Escolhe tipo aleatoriamente, retorna todas as palavras
    valores_dicionario_str = random.choice(list(dicionario.values()))
    palavras_categoria = []
    for i in valores_dicionario_str.split(','):
        palavras_categoria.append(i)

    # Escolhe palavra aleatoriamente

    palavras_escolhidas_rodada = random.sample(palavras_categoria,k=3)
    return palavras_escolhidas_rodada

#testando = sorteio()
#print(testando)
