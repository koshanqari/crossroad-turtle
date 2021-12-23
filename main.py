import time
from turtle import Screen, speed
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
NUM_OF_CARS = 10
#setting up scoreboard
score = Scoreboard()

#Setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("KQari's Road Crosser")

#Setting up player
player = Player()

#setting up car 
car = []
for i in range(NUM_OF_CARS):
    car.append(CarManager())



#Screen listening
screen.listen()
screen.onkey(player.move_up, "Up")






sleep_delay = 0.1
game_is_on = True
while game_is_on:
    time.sleep(sleep_delay)

    
    
    for i in range(NUM_OF_CARS):
        car[i].move_left()
        if car[i].xcor() < -300:
            car[i].car_reset()

    for i in range(NUM_OF_CARS):
        if player.distance(car[i].position()) < 20:
            game_is_on = False


    if player.ycor() > 280:
        score.update()
        player.reset_player()
        sleep_delay /= 2
        


    screen.update()
score.game_over()
screen.exitonclick()
