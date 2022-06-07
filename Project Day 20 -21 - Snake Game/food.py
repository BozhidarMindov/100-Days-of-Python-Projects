from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("cyan")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        rand_x = random.randint(-275, 275)
        rand_y = random.randint(-275, 275)
        self.goto(rand_x, rand_y)
