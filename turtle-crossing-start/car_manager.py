from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.all_cars = []
    

    def create_cars(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            random_car = Turtle(shape='square')
            random_car.shapesize(stretch_wid=1, stretch_len=2)
            random_car.penup()
            random_car.color(choice(COLORS))
            y = randint(-200, 200)
            random_car.setpos(x=300, y=y)
            self.all_cars.append(random_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE )

   