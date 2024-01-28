from turtle import Turtle
ALIGN="center"
FONT=('Arial', 26, 'normal') 

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white") 

        self.penup()
        self.goto(0,270) 
        self.hideturtle() 
        self.updated_score()
        #self.write(f" the score is :{self.score}", move=False, align='center', font=('Arial', 26, 'normal'))
       
    def updated_score(self):
        self.write(f" the score is :{self.score}", move=False, align=ALIGN, font=FONT)


    def inc_score(self):
        self.score+=1
        self.clear() 
        self.updated_score()
    def game_over(self): 
        self.penup()  
        self.goto(0,0)
        self.write("GAME OVER", move=False, align='center', font=('PressStart2P', 28, 'normal'))

     