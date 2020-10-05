# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
from clear_terminal import clear
import random
import string

# Board (tabuleiro)
from typing import List, Any

board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.letters_in = []
        self.letters_out = []
        self.letters = []
        self.cont = len(board)-1

    # Método para adivinhar a letra
    def guess(self, letter):

        self.letters.append(letter)

        if self.word.find(letter) >= 0:
            self.letters_in.append(letter)
        else:
            self.letters_out.append(letter)
            self.cont = self.cont-1


    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if self.cont == 0:
            return True
        return False

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if self.hide_word() == self.word:
            return True
        return False

    #Método para não mostrar a letra no board
    def hide_word(self):
        hide = ""
        for pos, i in enumerate(self.word):
           if i in self.letters_in:
               hide = hide + i
           else:
               hide = hide + "*"
        return hide

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
            print(board[self.cont])

            print(self.hide_word())

            print("Letras erradas: ", ', '.join(self.letters_out))
            print("Letras acertadas: ", ', '.join(self.letters_in))





# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Mostra tela com forca zerada e mensagens iniciais
    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter

    while not game.hangman_won() and not game.hangman_over():
        clear()
        game.print_game_status()
        letter = input("Digite uma letra: ")
        game.guess(letter)

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
