from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for i in range(3):
            tim = Turtle("square")
            tim.penup()
            a = -20 * i
            tim.goto(x=a, y=0)
            tim.color("white")
            self.segment.append(tim)

    def reset(self):
        for s in self.segment:
            s.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]
    def move(self):

        for segn in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[segn - 1].xcor()
            new_y = self.segment[segn - 1].ycor()

            self.segment[segn].goto(new_x, new_y)
        self.head.forward(20)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != UP:

            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:

            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:

            self.head.setheading(180)


    def add_seg(self, position):
        tim = Turtle("square")
        tim.penup()
        tim.goto(position)
        tim.color("white")
        self.segment.append(tim)

    def extend(self):
        self.add_seg(self.segment[-1].position())