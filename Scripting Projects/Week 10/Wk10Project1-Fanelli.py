#importing materials needed
import turtle
import math

#starting the function
def drawCircle(t, center_x, center_y, radius):
    circumference_distance = 2.0 * math.pi * radius / 120.0
    t.up()
    t.goto(center_x + radius, center_y)
    t.setheading(90)
    t.down()
    for _ in range(120):
        t.forward(circumference_distance)
        t.left(3)

#example function
myTurtle = turtle.Turtle()
drawCircle(myTurtle, 0, 0, 100)

