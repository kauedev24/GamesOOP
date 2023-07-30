from screen import config_screen, screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep


config_screen()
screen.tracer(0)

paddle = Paddle()
ball = Ball()
score = Scoreboard()

# Configurações das teclas.
screen.listen()
screen.onkeypress(paddle.goto_up_right, 'Up')
screen.onkeypress(paddle.goto_down_right, 'Down')
screen.onkeypress(paddle.goto_up_left, 'w')
screen.onkeypress(paddle.goto_down_left, 's')

game_is_on = True
while game_is_on:
    sleep(0.04)  # Velocidade da bolinha >> 0.04
    screen.update()
    ball.move()

    # Detecta quando a bola colide com a parede horizontal - Eixo Y
    if ball.ycor() > 230 or ball.ycor() < -230:
        #needs to bounce 
        ball.bounce_y()

    # Detecta quando a bola colide com as raquetes em todo seu espaço(distancia de 50px)
    if ball.distance(paddle.right_paddle) < 50 and ball.xcor() > 350 or ball.distance(paddle.left_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()
    
    # Detecta quando a bola colide com o lado direito, soma 1 ponto para o jogador do lado esquerdo.
    if ball.xcor() > 380:
        ball.reset_position()
        score.point_l()
   
    # Detecta quando a bola colida com o lado esquerdo, soma 1 ponto para o jogador do lado direito.
    if ball.xcor() < -380:
        ball.reset_position()
        score.point_r()

    if score.l_score > 10 or score.r_score > 10:  # Pontuação máxima para vencer cada rodada. >> 10
        break


screen.exitonclick()
