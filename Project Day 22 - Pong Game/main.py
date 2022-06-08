from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from draw_line import Draw_line
import time

#creating a screen and changing its size and behavior
screen = Screen()
screen.setup(height = 600, width = 800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#drawing a dotted line
new_line = Draw_line()

#creating paddles and a ball object
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
#---------------------------------------------

game_end = False
while game_end == False:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with a wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    
    #detect collision with the paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #detect when the right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    #detect when the left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
