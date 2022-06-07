from turtle import Turtle, Screen
import random

import turtle as t
t.title("Turtle Racing Game")
t.Screen().bgcolor("DarkSlateGray1")
screen = Screen()
screen.setup(width = 700, height = 600)

start_game = False
colors = ["red", "orange", "green", "yellow", "blue", "purple"]
y_positions = [-170, -100, -30, 40, 110, 180]
turtle_list = []

user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
if not user_bet:
    t.Screen().bye()

for turtle in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.turtlesize(2)
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-330, y = y_positions[turtle])
    turtle_list.append(new_turtle)

if user_bet:
    start_game = True

while start_game:
    for turtle in turtle_list:
        if turtle.xcor() > 310:
            start_game = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You won! The {winner_color} turtle is the winner!")
            else:
                print(f"You lost! The {winner_color} turtle is the winner!")

        step = random.randint(0, 10)
        turtle.forward(step)

screen.exitonclick()
