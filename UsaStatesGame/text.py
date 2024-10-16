from turtle import Turtle
FONT = ("Arial", 10, "normal")


class Text(Turtle):
    def __init__(self, xcor, ycor, name, color):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.teleport(xcor, ycor)
        self.color(color)
        self.write(font=FONT, align="center", arg=name)

    def game_over(self):
        self.teleport(0, 0)
        self.write(font=("Arial", 25, "normal"), align="center", arg="Game completed!")
