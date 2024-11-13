# import colorgram
import random
import turtle

tim = turtle.Turtle()
turtle.colormode(255)

# colors_from_painting = colorgram.extract("damien_hirst_andromeda.jpg", 10)
# colors = []
#
# for color in colors_from_painting:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     colors.append(rgb)
#
# print(colors)

colors = [(125, 177, 198), (212, 224, 233), (37, 117, 150), (195, 139, 166), (171, 82, 43), (161, 58, 87), (191, 88, 128), (203, 162, 98), (55, 156, 175), (226, 200, 210)]

tim.hideturtle()
tim.speed(0)
tim.penup()
y_number = -220

for _ in range(10):
    tim.teleport(-300, y_number)
    y_number += 50
    for _ in range(10):
        tim.forward(50)
        tim.dot(20, random.choice(colors))

screen = turtle.Screen()
screen.exitonclick()
