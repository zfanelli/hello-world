"""
Program file: Wk10Project2-Fanelli
Author: Zane Fanelli
This program prompts the user for the level of a c-curve
and draws a c-curve of that level with line segments in random colors.
"""

from turtle import Turtle, tracer, update
import random

def cCurve(t, x1, y1, x2, y2, level):
    """Draws a c-curve of the given level with line segments in random colors."""
    if level == 0:
        drawLine(t, x1, y1, x2, y2)
    else:
        xm = (x1 + x2 + y1 - y2) // 2
        ym = (x2 + y1 + y2 - x1) // 2
        cCurve(t, x1, y1, xm, ym, level - 1)
        cCurve(t, xm, ym, x2, y2, level - 1)

def drawLine(t, x1, y1, x2, y2):
    """Draws a line segment between the end points with a random color."""
    t.pencolor(random.random(), random.random(), random.random())
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)

def main():
    level = int(input("Enter the level (0 or greater): "))
    t = Turtle()
    if level > 8:
        tracer(False)
        t.hideturtle()
    cCurve(t, 50, -50, 50, 50, level)
    if level > 8:
        update()

if __name__ == "__main__":
    main()
