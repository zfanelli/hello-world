import turtle

def drawKochSnowflake(t, distance, level):
    for _ in range(3):
        drawFractalLine(t, distance, level)
        t.right(120)

#drawing the fractal line
def drawFractalLine(t, distance, level):
    if level == 0:
        t.forward(distance)
    else:
        drawFractalLine(t, distance/3, level-1)
        t.left(60)
        drawFractalLine(t, distance/3, level-1)
        t.right(120)
        drawFractalLine(t, distance/3, level-1)
        t.left(60)
        drawFractalLine(t, distance/3, level-1)

def main():
    level = int(input("Enter the level of Koch snowflake (0 or greater): "))
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    t.speed(0)
    t.penup()
    t.goto(-150, 100)
    t.pendown()
    t.color("blue")
    drawKochSnowflake(t, 300, level)
    screen.mainloop()

if __name__ == "__main__":
    main()
