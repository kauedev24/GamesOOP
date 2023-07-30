from turtle import Screen

screen = Screen()
def config_screen():
    """Configurações da tela."""
    screen.setup(width=9000, height=500)
    screen.bgcolor('black')
    screen.title('Pong')

