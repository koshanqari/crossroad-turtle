import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


#Setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("KQari's Road Crosser")

#Setting up player
player = Player()

#setting up car 
car = CarManager()

#Screen listening
screen.listen()
screen.onkey(player.move_up, "Up")






game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.move_left()
    if car.xcor() < -300:
        car.car_reset()
    screen.update()
