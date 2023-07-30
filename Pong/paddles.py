import turtle as t

COORDINATE = 370

class Paddle:

    def __init__(self):
        self.paddles = []
        self.create_paddles()
        self.right_paddle = self.paddles[0]
        self.left_paddle = self.paddles[1]
       
        
    def create_paddles(self):
        """Cria duas raquetes."""
        t.mode('logo')
        for _ in range(2):
            paddle = t.Turtle(shape='square')
            paddle.shapesize(stretch_wid=1, stretch_len=5)
            paddle.color('white')
            paddle.penup()
            if _ == 0:
                paddle.goto(x=COORDINATE, y=0)  # Valor POSITIVO >> DIREITA
            elif _ == 1:
                paddle.goto(x=-COORDINATE, y=0)  # Valor NEGATIVO >> ESQUERDA
            self.paddles.append(paddle)


    def goto_up_right(self):
        """Movimento para cima da raqueta direita."""
        self.right_paddle.setheading(0)
        self.right_paddle.forward(20)


    def goto_down_right(self):
        """Movimento para baixo da raqueta direita."""
        self.right_paddle.setheading(180)
        self.right_paddle.forward(20)
    

    def goto_up_left(self):
        """Movimento para cima da raqueta esquerda."""
        self.left_paddle.setheading(0)
        self.left_paddle.forward(20)
        

    def goto_down_left(self):
        """Movimento para baixo da raqueta esquerda."""
        self.left_paddle.setheading(180)
        self.left_paddle.forward(20)
    
 