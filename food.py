
from turtle import Turtle

import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("green")
        self.speed("fastest")
        self.refr()


    def refr(self):
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x, y)