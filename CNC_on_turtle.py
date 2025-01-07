import turtle
import ast

turtle.Screen().bgcolor("white")

t = turtle.Turtle()
t.speed(100)
t.pensize(1)

zero_x = -100
zero_y = -300

f = open("data_dio.jpg.txt", "r")
mass = ast.literal_eval(*f)
for h in mass:    
    if h[2] == "w":
        t.penup()
    elif h[2] == "b":
        t.pendown()
    t.goto(h[0]+zero_x, h[1]+zero_y)


