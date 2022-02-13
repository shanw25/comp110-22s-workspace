from turtle import Turtle, colormode, done
colormode(255)
side_length: float = 300
leo: Turtle = Turtle()
leo.penup()
leo.goto(45, 60)
leo.pendown()
leo.pencolor("pink")
leo.speed(600)
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()
bob.penup()
bob.goto(45, 60)
bob.pendown()
bob.pencolor(255, 0, 0)
leo.speed(60)

c: int = 0
while (c < 300):
    bob.forward(side_length)
    bob.left(120)
    side_length = side_length * 0.97
    c = c + 1