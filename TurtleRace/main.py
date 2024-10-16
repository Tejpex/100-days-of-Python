from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput("Make a bet", "What color turtle do you think will win the game:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_number = 150

for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.teleport(-230, y_number)
    y_number -= 50
    turtles.append(turtle)

if user_bet:
    is_race_on = True

winning_turtle = ""

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(2, 40))
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            is_race_on = False

if winning_turtle == user_bet.lower():
    print("You win!")
else:
    print(f"Sorry, the winning turtle was {winning_turtle}.")

screen.exitonclick()
