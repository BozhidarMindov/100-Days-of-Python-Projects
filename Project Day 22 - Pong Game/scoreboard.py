from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.left_score = 0
        self.right_score = 0
        #self.create_scoreboard()
        self.update_scoreboard()
    
    def create_scoreboard(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.left_score = 0
        self.right_score = 0
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)
    
    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()
    
    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()
