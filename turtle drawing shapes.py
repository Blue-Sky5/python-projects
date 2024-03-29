from turtle import Turtle, Screen
import random

colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy"
    , "blue", "skyblue", "cyan", "turquoise","lightgreen", "green"]
dir = [0,90,180,270]

pen = Turtle()
pen.speed("fastest")

for i in range(1000):
    pen.color(random.choice(colors))
    pen.circle(45)
    pen.right(20)


panel = Screen()
panel.exitonclick()


