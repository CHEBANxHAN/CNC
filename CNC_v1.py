from PIL import Image, ImageDraw, ImageGrab
import turtle

turtle.Screen().bgcolor("white")

t = turtle.Turtle()
t.speed(100)
t.pensize(1)


zero_x = -100
zero_y = 300

name = "example/dio.jpg"
nameX = 500
nameY = 500
img = Image.open(name).convert('1')
img = img.resize((nameX, nameY))
mass = list(img.getdata())

count = 0
a = []
data = []

for h in mass:
    count += 1
    a.append(h)
    if count >= nameX:
        data.append(a)
        a = []
        count = 0
        
count_x = 0
count_y = 0

mass_coord = []
coord = []

for i in data:
    for j in i:
        if j == 0:
            coord.append(count_x)
            coord.append(count_y)
            coord.append("b")
            mass_coord.append(coord)
        if j == 255:
            coord.append(count_x)
            coord.append(count_y)
            coord.append("w")
            mass_coord.append(coord)
        coord = []
        count_x += 1
    count_x = 0
    count_y -= 1 #Ставим + если ось ординат направленна вверх, - если вниз

for h in mass_coord:    
    if h[2] == "w":
        t.penup()
    elif h[2] == "b":
        t.pendown()
    t.goto(h[0]+zero_x, h[1]+zero_y)
