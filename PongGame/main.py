import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(-360, 0)
right_paddle = Paddle(350, 0)
screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

line = Turtle("square")
line.hideturtle()
line.teleport(0, 300)
line.setheading(270)
line.color("white")
line.pensize(7)
for _ in range(15):
    line.forward(20)
    line.penup()
    line.forward(20)
    line.pendown()

ball = Ball()
l_score = Scoreboard(-50)
r_score = Scoreboard(50)

game_is_on = True
while game_is_on:
    time.sleep(0.03)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_of_wall()
    if ball.distance(left_paddle) < 50 and ball.xcor() <= -340:
        ball.bounce_of_left()
        ball.increase_speed()
    if ball.distance(right_paddle) < 50 and ball.xcor() >= 330:
        ball.bounce_of_right()
        ball.increase_speed()
    if ball.xcor() >= 400:
        ball.goto(0, 0)
        l_score.update_score()
        ball.speed_setting = 10
        time.sleep(0.5)
        ball.setheading(random.randint(160, 180))
    if ball.xcor() <= -400:
        ball.goto(0, 0)
        r_score.update_score()
        ball.speed_setting = 10
        time.sleep(0.5)
        ball.setheading(random.randint(0, 20))

turtle.mainloop()
