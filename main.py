from time import sleep
from turtle import Screen

from food import Food
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

game_in_progress = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_in_progress:
    screen.update()
    sleep(0.1)
    snake.move_forward()

    #Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh_food()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with the wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() <-280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        scoreboard.game_over_txt()
        game_in_progress = False

    #Detect tail hit
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.game_over_txt()
            game_in_progress = False















screen.exitonclick()