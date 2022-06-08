import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#creating a screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

#creating a player, a car manager and a scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

#while loop that represents the game movement
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    #detecting collision with a car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
        
    #detect if the turtle has reached the top
    if player.player_crossed() == True:
        scoreboard.increase_level()
        player.restart()
        car_manager.level_up()
        

screen.exitonclick()
