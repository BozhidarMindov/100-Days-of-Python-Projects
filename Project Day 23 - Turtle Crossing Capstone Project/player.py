from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()
    
    def create_player(self):
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.restart()
    
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def player_crossed(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    
    def restart(self):
        self.goto(STARTING_POSITION)
