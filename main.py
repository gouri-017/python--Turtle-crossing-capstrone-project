from turtle import Screen
from car_manager import Cars, STARTING_MOVE_DISTANCE
from scoreborad import Scoreboard
from player import Player, FINISH_LINE_Y, START_POSITION
import time
import random



screen=Screen()
screen.setup(600,600)
screen.tracer(0)
screen.title("Turtle Crossing Game")

p1=Player()
new_car=Cars()
score=Scoreboard()


screen.listen()
screen.onkey(p1.up,"Up")

i = 0
on=True
while on:
    time.sleep(0.1)
    screen.update()
    new_car.create_car()
    new_car.move()
    for car in new_car.all_cars:
        if car.distance(p1)<20:
         on=False
         score.game_over()
         break
        if p1.ycor() == FINISH_LINE_Y:
         p1.goto(START_POSITION)
         new_car.level_up()
         score.add_score()




screen.exitonclick()