from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        """Definindo a bola."""
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10


    def move(self):
        """Movimentação constante da bolinha a partir da soma das coordenadas"""
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)


    def bounce_y(self):
        """Multiplica-se por menos 1 para alterar a direção da bolinha com a soma das coordenadas."""
        self.y_move *= -1
    
    
    def bounce_x(self):
        """Multiplica-se por menos 1 para alterar a direção da bolinha com a soma das coordenadas."""
        self.x_move *= -1


    def reset_position(self):
        """Retorna a bola para a posição inicial e na direção oposta a que estava(Bounce), a cada ponto."""
        self.goto(0,0)
        self.bounce_x()

