from turtle import Turtle

SQUARE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    #class initialization
    def __init__(self):
        self.square_list = []
        self.create_snake()
        self.head = self.square_list[0]

    #adding a new square to the snake
    def add_square(self, position):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.square_list.append(new_square)

    #extending the snake
    def extend(self):
        self.add_square(self.square_list[-1].position())

    #creating the snake
    def create_snake(self):
        for square in SQUARE_POSITIONS:
            self.add_square(square)

    #moving the snake forward
    def move(self):
        for sqr_num in range(len(self.square_list) - 1, 0, -1):
            new_x = self.square_list[sqr_num - 1]. xcor()
            new_y = self.square_list[sqr_num - 1]. ycor()
            self.square_list[sqr_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    #moving the snake up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    #moving the snake down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    #moving the snake left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    #moving the snake right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    


