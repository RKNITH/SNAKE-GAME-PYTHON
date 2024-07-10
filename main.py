from turtle import Turtle, Screen
import time
from food import Food
from scoreboard import Score
from snake import Snake

screen =Screen()
food =Food()
score =Score()
snake =Snake()

screen.tracer(0)
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("snake game")




screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")





is_game_on =True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) <15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() >290 or snake.head.xcor() <-290 or snake.head.ycor() >290  or snake.head.ycor() <-290:
        snake.reset()
        score.reset_score()


    for seg in snake.segment[1:]:
        if snake.head.distance(seg) <10:
           snake.reset()
           score.reset_score()





















screen.mainloop()