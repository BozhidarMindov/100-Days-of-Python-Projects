from turtle import Turtle

class Draw_line(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.fillcolor("white")
        self.setheading(270)
        self.penup()
        self.goto((0, 300))
        self.pendown()
        self.draw_dotted_line()
        self.hideturtle()
    
    def draw_dotted_line(self):
        for i in range(0, 10):
            self.forward(50)
            self.penup()
            self.forward(10)
            self.pendown()
