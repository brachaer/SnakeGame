from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)

my_snake = Snake()
my_food=Food()
my_score= Score()
my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")

game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()
    if my_snake.head.distance(my_food)<15:
        my_food.refresh()
        my_snake.extend()
        my_score.increase_score()

    if my_snake.head.xcor()>280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280  :
        # game_is_on = False
        my_score.reset()
        my_snake.reset()

    for segment in my_snake.snake[1:]:
        if my_snake.head.distance(segment) < 10:
            my_score.reset()
            my_snake.reset()

my_screen.exitonclick()
