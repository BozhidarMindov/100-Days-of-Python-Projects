from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import random

#screen behavior and snake, snake_food and scoreboard declaration
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
#--------------------------

game_end = False
while game_end == False:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 12:
        food.refresh()
        snake.extend()
        scoreboard.update_scoreboard()

    #detect collision with a wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_end = True
        scoreboard.game_over()
    
    #detect collision with the tail
    for square in snake.square_list[1:]:
        if snake.head.distance(square) < 10:
            game_end = True
            scoreboard.game_over()

screen.exitonclick()