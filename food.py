from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__() 
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6,stretch_wid=0.6)
        self.speed("fastest")
        self.refresh() 
    def refresh(self):
        sexy_x=random.randint(-270,270)
        sexy_y=random.randint(-270,270)
        self.goto(sexy_x,sexy_y)
