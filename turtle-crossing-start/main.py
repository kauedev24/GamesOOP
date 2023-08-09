import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Key settings
screen.listen()
screen.onkeypress(player.move, 'Up')

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect when the user advances to the next level
    if player.ycor() >= 280:
        player.restart_position()
        scoreboard.points()
        scoreboard.update_score()

    # Detect when the car hits the turtle  
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            
screen.exitonclick()
