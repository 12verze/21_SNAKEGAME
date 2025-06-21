from turtle import *
import time
from snake import *
from food import *
from scoreboard import *


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkey(snake.up, "Up")

screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_on= True
while is_on:
    screen.update()
    time.sleep(0.075)
    snake.move()

    #coll with food
    if snake.head.distance(food)< 15:
        food.refr()
        snake.extend()
        score.increase()

    #coll with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor()> 290 or snake.head.ycor()< -290:
        score.reset()
        snake.reset()
        # is_on = False
        # score.game0ver()

    #coll with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            # is_on = False
            # score.game0ver()
            score.reset()
            snake.reset()


















# screen.listen()
# def front():
#     segment[0].forward(20)
#
#
# def left():
#     segment[0].left(90)
#
# def right():
#     segment[0].right(90)
#
#
# screen.listen()
# def run():
#
#     screen.onkeypress(front, "w")
#     screen.onkeyrelease(front, "w")
#     screen.onkeypress(left, "a")
#     screen.onkeyrelease(left, "a")
#     screen.onkeypress(right, "w")
#     screen.onkeyrelease(right, "w")
#
#
# while is_on:
#     run()
#     segment[2].goto(segment[0].pos())
#     segment[1].goto(segment[1].pos())
#     screen.update()
#     time.sleep(0.1)











screen.exitonclick()

