from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(random.randint(0, 20))
        self.speed_setting = 10

    def move(self):
        self.forward(self.speed_setting)

    def bounce_of_wall(self):
        new_direction = 360 - self.heading()
        self.setheading(new_direction)

    def bounce_of_left(self):
        if 180 >= self.heading() >= 90:
            new_direction = 180 - self.heading()
        elif 270 >= self.heading() >= 180:
            new_direction = 180 + (360 - self.heading())
        else:
            new_direction = self.heading()
        self.setheading(new_direction)

    def bounce_of_right(self):
        if 90 >= self.heading() >= 0:
            new_direction = 180 - self.heading()
        elif 360 >= self.heading() >= 270:
            new_direction = 180 + (360 - self.heading())
        else:
            new_direction = self.heading()
        self.setheading(new_direction)

    def increase_speed(self):
        self.speed_setting += 1
