from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.add_car()
        self.speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        car = Turtle("square")
        car.color(COLORS[random.randint(0, 5)])
        car.shapesize(1, 2)
        car.setheading(180)
        car.penup()
        car.teleport(300, random.randint(-240, 240))
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
