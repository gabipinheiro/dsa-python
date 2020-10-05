# Roletrando
# Organizacao das palavra por tipo

def dict_palavras():
    with open("tipo_palavras.txt") as f:
        palavras = f.read()
        palavras_tipo = palavras.split('\n')

    # Criação de dicionario"

    # Lista contendo lista tipo/palavra
    lista_tipo_palavra = []
    for i in palavras_tipo:
        i = i.strip(')')
        lista_tipo_palavra.append(i.split('('))

    # Montando o dicionário com a lista criada acima
    dict_tipo_palavra = {}
    for j in lista_tipo_palavra:
        dict_tipo_palavra[j[0]]=j[1]

    return dict_tipo_palavra

#gabi = dict_palavras()
#print(gabi)