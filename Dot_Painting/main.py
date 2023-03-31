import colorgram
import random
import turtle as t

PICTURE_NAME = 'color_landscape.jpg'

colors = colorgram.extract(PICTURE_NAME, 30)
print(colors)
rgb_colors = list()
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

tim = t.Turtle()
screen = t.Screen()
screen.colormode(255)
space_between = 50
number_of_columns = 10
number_of_rows = 10
tim.penup()
tim.back(250)
tim.right(90)
tim.forward(250)
tim.left(90)

for i in range(number_of_rows):
    for j in range(number_of_columns):
        color = random.choice(rgb_colors)
        tim.dot(20, color)
        tim.forward(space_between)
        j = j + 1
    tim.left(90)
    tim.forward(space_between)
    tim.left(90)
    tim.forward(space_between * number_of_columns)
    tim.left(180)
    i = i + 1

tim.hideturtle()
screen.exitonclick()