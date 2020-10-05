# Robô
# Main

# Import

UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"
QUIT = "QUIT"

class robot():

    def __init__(self):
        self.pos = [0, 0]
        print("Robô criado com sucesso")

    def walk(self,move):
        #  andamento do robô dependendo da resposta do usuario
        if move == UP:
            # linha
            if self.pos[0] > 0:
                self.pos[0] = self.pos[0] - 1
                #self.pos[1] = self.pos[1]

        if move == RIGHT:
            # linha
            if self.pos[1] < 4:
                #self.pos[0] = self.pos[0]
                self.pos[1] = self.pos[1] + 1

        if move == DOWN:
            # linha
            if self.pos[0] < 4:
                self.pos[0] = self.pos[0] + 1
                #self.pos[1] = self.pos[1]

        if move == LEFT:
            # linha
            if self.pos[1] > 0:
                #self.pos[0] = self.pos[0]
                self.pos[1] = self.pos[1] - 1

    def grade(self):
        # grade zerada
        grade = []
        for i in range(0, 5):
            grade = grade + [[""] * 5]

        grade[self.pos[0]][self.pos[1]] = "R"

        for i in grade:
            print(i)

    def over(self):
        if self.pos[0]==4 and self.pos[1]==4:
            print("terminou")
            return True
        else:
            print("não terminou")
            return False

    def status(self):
        self.grade()

def get_key_pressed(letra):
    # Conversao letra pra movimentacao

    if letra == "J":
        return LEFT

    if letra == "K":
        return DOWN

    if letra == "I":
        return UP

    if letra == "L":
        return RIGHT

    if letra == "Q":
        return QUIT

def main():
    meu_robo = robot()
    meu_robo.grade()
    move = ""
    while (meu_robo.over() == False) and (move != QUIT):
        press = input("Ande com o robô: \nI: pra cima; \nK: pra baixo; \nJ: pra esquerda; \nL: pra direita; \nQ: fim\n")
        move = get_key_pressed(press)
        meu_robo.walk(move)
        meu_robo.status()



    print("Jogo Encerrado")
# Executa o programa
if __name__ == "__main__":
    main()
