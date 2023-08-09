from turtle import Turtle

FONT = ("arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = 1
        self.penup()
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(x=-270, y=250)
        self.write(f"Level: {self.counter}", True, font=FONT)


    def points(self):
        self.counter += 1


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=FONT)

