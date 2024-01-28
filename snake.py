from turtle import Turtle

START = [(0, 0), (-20, 0), (-40, 0)]
DIST = 20

class Snake:
    def __init__(self):
        self.parts = []  # Fix syntax error here
        self.snake_time()
        self.head = self.parts[0]

    def snake_time(self):
        for position in START:
            self.add_seg(position)
            

    def add_seg(self,position):
            sexy_part = Turtle("square")
            sexy_part.color("white")
            sexy_part.penup()
            sexy_part.goto(position)
            self.parts.append(sexy_part)


    def extend(self):
        self.add_seg(self.parts[-1].position())

    # Example usage:
    def move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[i - 1].xcor()
            new_y = self.parts[i - 1].ycor()
            self.parts[i].goto(new_x, new_y)
        self.head.forward(DIST)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def rt(self):
        self.head.setheading(0)

    def lt(self):
        self.head.setheading(180)
