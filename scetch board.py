from turtle import Turtle, Screen
from turtle import Turtle, Screen
pen = Turtle()


def forward():
    pen.forward(10)


def backward():
    pen.back(10)


def turn_l():
    pen.left(10)


def turn_r():
    pen.right(10);


panel = Screen()
panel.listen()
panel.onkey(forward, "Right")
panel.onkey(backward, "Left")
panel.onkey(turn_l, "Up")
panel.onkey(turn_r, "Down")
panel.exitonclick()