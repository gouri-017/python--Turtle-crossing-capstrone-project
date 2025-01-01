from turtle import Turtle

FONT=('courier',18,'normal')


class Scoreboard(Turtle):
    def __init__(self):
     super().__init__()
     self.color('black')
     self.penup()
     self.hideturtle()
     self.level= 1
     self.update()

    def update(self):
        self.clear()
        self.goto(-150, 240)
        self.write(f"Level:{self.level} ",False,"center",FONT)

    def add_score(self):
        self.level+=1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",False,"center",FONT)
