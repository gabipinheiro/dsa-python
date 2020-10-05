# Roletrando
# Main

# Import
from ROLETRANDO.sorteio_palavras import sorteio
from clear_terminal import clear

class rol:

    # Método Construtor
    def __init__(self,word,players):
        self.word = word
        self.players = players
        self.letters_in = []
        self.letters_out = []
        self.letters = []
        self.point = [0 for i in range(0,len(players))]
        self.words_yes = [0, 0, 0]
        # action=0 para adivinhar letra, action=1 para adivinhar palavra
        self.action = 1
        # para saber qual jogador está no momento
        self.pos_player = 0

    # Verificar se letra existe nas palavras e soma pontuação dos jogadores
    def guess_letter(self, letter,player):

        # Verificação das letras nas palavras
        self.letters.append(letter)
        self.pos_player = player

        for i in self.word:
            if letter not in self.letters_in:
                if letter not in i:
                    if letter not in self.letters_out:
                        self.letters_out.append(letter)
                elif letter in i:
                    self.letters_in.append(letter)
                    if letter in self.letters_out:
                        self.letters_out.remove(letter)

        # Pontuação dos jogadores
        if letter in self.letters_in:
            #self.point[player] = self.point[player]+1
            for pos,i in enumerate(self.word):
                count_per_word = i.count(letter)
                self.point[player] = self.point[player] + count_per_word
            self.point[player] = self.point[player]*10

    # Verificar se palavras foram advinhadas
    def guess_word(self, words_guessed,player,action):

        self.pos_player = player

        for pos,i in enumerate(self.word):
            for j in words_guessed:
                if j == i:
                    self.words_yes[pos] = 1

        # Pontuação do vencedor quando advinhar a palavra = 100%
        count_all_letters = 0
        if self.words_yes == [1,1,1]:
            for i in self.word:
                count_all_letters = count_all_letters + len(i)
            self.point[player] = count_all_letters * 10

        self.action = action
        return player

    # Retorna palavras apenas com letras adivinhadas
    def hide_word(self):

        hide = []
        for k in self.word:
            hide.append("")

        for pos, i in enumerate(self.word):
            for j in i:
                if j in self.letters_in:
                    hide[pos] = hide[pos] + j
                else:
                    hide[pos] = hide[pos] + "*"
        return hide

    def won(self):

        # Possibilidades de sucesso do jogo
        if self.hide_word() == self.word:
            return True
        elif self.words_yes == [1,1,1]:
            return True
        return False

    def over(self):

        if self.action == 2 and self.words_yes != [1,1,1]:
            return True
        return False

    def winner(self):
        if self.action == 2:
            ultima_pos_lista_players = len(self.players)-1
            if self.pos_player == ultima_pos_lista_players:
                #ganhador = 0
                self.pos_player == 0
            else:
                #ganhador = self.pos_player + 1
                self.pos_player == self.pos_player + 1
        elif self.action == 1:
            point_winner = max(self.point)
            self.pos_player == self.point.index(point_winner)
            #ganhador = self.point.index(point_winner)

        return self.players[self.pos_player]

    def print_status(self):

        # Imprime palavras dependendo se o jogador ganhou.
        if self.won() is True:
            print("\n", self.word)
            print("\nO ganhador foi %s com o total de %i pontos" % (self.winner(), max(self.point)))
            pass
        elif self.action==2 and self.words_yes != [1,1,1]:
            vencedor = self.winner()
            print(vencedor)
            print("\n, palavras erradas. \nO vencedor foi %s com %i pontos: " % (vencedor,self.point[self.pos_player]))
            pass
        else:
            print("\n", self.hide_word())

        # Imprime letras
        print("\nLetras acertadas: ",self.letters_in)
        print("Letras erradas: ",self.letters_out)

        # Imprime pontuação
        print("\nPontuação:")

        for pos,i in enumerate(self.players):
            print(i,": ", self.point[pos])



def main():

    # Pede quantidade e nome dos jogadores
    players_qtdd = int(input("Digite quantos jogadores terão nesta rodada: "))

    players = []
    for i in range(0, players_qtdd):
        nome = input("Escreva nome do jogador %d: " % (i + 1))
        players.append(nome)

    # Inicia jogo
    game = rol(sorteio(),players)
    print(game.word)

    while not game.won() and not game.over():
        game.print_status()

        for pos,i in enumerate(players):
            choice_action = int(input("\n%s, escolha uma opção:\n1: Chutar uma letra;\n2: Advinhar palavras.\n" %i))
            if choice_action == 1:
                letter = input("\nDigite uma letra: \n")
                game.guess_letter(letter, pos)
            else:
                print("Digite as palavras?")
                word_1 = input("1ª: ")
                word_2 = input("2ª: ")
                word_3 = input("3ª: ")
                words_guess = [word_1, word_2, word_3]
                game.guess_word(words_guess, pos, choice_action)

            clear()
            game.print_status()

    print("\nFim de jogo\n")

# Executa o programa
if __name__ == "__main__":
    main()

