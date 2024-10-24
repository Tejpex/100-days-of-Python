from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("firebrick")
        self.penup()
        self.relocate()

    def relocate(self):
        x_position = random.randint(-270, 270)
        y_position = random.randint(-270, 270)
        self.teleport(x_position, y_position)
