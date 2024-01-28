from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score 

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Sexy Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score=Score()
screen.listen() 
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.rt, "Right")
screen.onkey(snake.lt, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    # Move the snake
    snake.move()
# collision with food
    if snake.head.distance(food)<15:
        food.refresh() 
        snake.extend() 
        score.inc_score()
 
    # Add your collision logic with wall if needed
    if snake.head.xcor()>280 or snake.head.ycor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280:
        score.game_over() 
        game_on=False 

#collision with its tail
        for i in snake.parts: 
            if i==snake.head:
                pass 
            elif snake.head.distance(i)<10:
                game_on=False
                score.game_over()
    
    
        
   

  

screen.mainloop()
