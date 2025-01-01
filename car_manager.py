from turtle import Turtle
import random


# numbers = [5, 4, 7, 15, 30, 20, ]
COLORS=['red','orange','yellow','green','purple','blue']
STARTING_MOVE_DISTANCE= 5
MOVE_INCR = 30


class Cars(Turtle):
    def __init__(self):
        self.all_cars=[]
        self.car_speed= STARTING_MOVE_DISTANCE
        # self.penup()
        # self.shape('square')
        # self.shapesize(1,2)
        # self.color(random.choice(COLORS))
        # self.goto(300,y)


    def create_car(self):
        random_no=random.randint(1,6)
        if random_no == 1:
            car=Turtle("square")
            car.penup()
            car.shapesize(1,2)
            car.color(random.choice(COLORS))
            y=random.randint(-220,220)
            car.goto(300, y)
            self.all_cars.append(car)

    def move(self):
        for j in self.all_cars:
            j.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed+= MOVE_INCR
