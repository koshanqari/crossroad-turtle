from time import sleep
from tkinter.constants import CENTER
from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-30, 250)
        self.score = -1
        self.update()
        
    
    def update(self):
        self.goto(0, 250)
        self.clear()
        self.score +=1
        self.write(f"LEVEL: {self.score}", font=FONT, align=CENTER)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", font= FONT, align=CENTER)
        self.goto(0,-20)
        self.write(f"Thank You for playing K.Qaris Cross Road", FONT, align=CENTER)

    
