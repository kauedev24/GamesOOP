from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        """Definindo o placar na tela."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.screen_()
       

    def screen_(self):
        """Atualização do placar a cada ponto."""
        self.clear()
        self.goto(0, 140)
        self.write(f"{self.l_score} | {self.r_score}", align='center', font=('Courier', 50, 'normal'))


    def point_l(self):
        """Ponto para o jogador do lado esquerdo."""
        self.l_score += 1
        self.screen_()


    def point_r(self):
        """Ponto para o jogador do lado direito."""
        self.r_score += 1   
        self.screen_() 

