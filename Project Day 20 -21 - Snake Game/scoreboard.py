from turtle import Turtle
ALIGNMENT ="center"
FONT = ("Courier", 22, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.create_scoreboard()
    
    def create_scoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)
    
    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.create_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
