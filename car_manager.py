import turtle
from random import choice, randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setheading(180)
        self.color(choice(COLORS))
        self.goto(randint(-300, 300), randint(-260, 280))
    
    def move_left(self):
        self.fd(MOVE_INCREMENT)

    def car_reset(self):
        self.goto(randint(300, 900), randint(-260, 280))