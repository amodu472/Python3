import turtle
from turtle import Turtle, Screen
from random import choice


gbenga = Turtle("turtle")
turtle.colormode(255)

# import colorgram
#
# colors = colorgram.extract("Damien Hirst.jpg", 30)
#
# rgb_list = []
#
# for _ in range(29):
#     color = colors[_]
#     rgb = color.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     r_g_b = (r, g, b)
#     rgb_list.append(r_g_b)
#
# print(rgb_list)

color_list = [(234, 251, 243), (197, 13, 32), (249, 237, 21), (39, 77, 188), (238, 227, 5), (39, 216, 68),
              (228, 160, 47), (243, 247, 253), (28, 40, 155), (214, 75, 14), (16, 153, 17), (199, 15, 11),
              (242, 34, 164), (226, 19, 120), (74, 9, 31), (60, 15, 8), (223, 141, 208), (11, 97, 62), (220, 160, 10),
              (18, 18, 43), (52, 211, 230), (11, 228, 239), (80, 73, 214), (238, 156, 217), (73, 212, 168),
              (81, 234, 202), (61, 233, 241)]

gbenga.hideturtle()
gbenga.penup()
gbenga.goto(-225, -225)

cord = gbenga.pos()
y_cord = cord[1]

for _ in range(10):
    for i in range(10):
        gbenga.dot(20, choice(color_list))
        gbenga.fd(50)

    y_cord += 50
    gbenga.goto(-225, y_cord)

screen = Screen()
screen.exitonclick()