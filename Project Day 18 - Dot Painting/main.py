import colorgram
import turtle as t
import random

color_list = [(58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (142, 178, 203), (139, 82, 105), (208, 90, 69), (237, 225, 233), (188, 80, 120), (69, 105, 90), (133, 182, 135),
              (133, 133, 74), (64, 156, 92), (47, 156, 193), (183, 192, 201), (213, 177, 191), (19, 58, 92), (20, 68, 113), (113, 123, 149), (227, 174, 166), (172, 203, 183), (156, 206, 217), (69, 58, 47), (72, 64, 53), (111, 46, 59), (53, 70, 64)]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(350)
tim.setheading(0)
num_dots = 101

for i in range(1, num_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if i % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()