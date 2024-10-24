from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()

score = Scoreboard()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")


def start_new_game():
    score.reset_game()
    snake.reset_snake()
    time.sleep(1.5)


game_is_on = True
while game_is_on:
    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.relocate()
        score.update_score()
        snake.extend()

    # Move about the screen
    snake.move()
    time.sleep(0.1)
    screen.update()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        start_new_game()

    # Detect collision with tail
    for segment in snake.snake_segments[2:]:
        if snake.head.distance(segment) < 10:
            start_new_game()

screen.exitonclick()
