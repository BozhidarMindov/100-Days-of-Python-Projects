from turtle import Turtle
ALIGNMENT ="center"
FONT = ("Courier", 22, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        #getting the previous high score of the game
        with open("highscore.txt") as file:
            self.high_score = int(file.read())

        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.create_scoreboard()
    
    def create_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align = ALIGNMENT, font = FONT)
    
    def update_scoreboard(self):
        self.score += 1
        self.create_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score

            #opening the high score file and updating the high score of the game
            with open ("highscore.txt", mode= "w") as write_file:
                write_file.truncate()
                write_file.write(str(self.high_score))
        self.score = 0
        self.create_scoreboard()
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
