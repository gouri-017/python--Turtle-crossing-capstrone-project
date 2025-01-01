from turtle import Turtle

START_POSITION= (0, -250)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(START_POSITION)


    def up(self):
        self.forward(MOVE_DISTANCE)

