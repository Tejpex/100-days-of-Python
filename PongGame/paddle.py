from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.teleport(xcor, ycor)

    def go_up(self):
        if self.ycor() < 275:
            new_y = self.ycor() + 25
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -275:
            new_y = self.ycor() - 25
            self.goto(self.xcor(), new_y)
