from turtle import Turtle
FONT = ("Courier", 42, "normal")


class Scoreboard(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.teleport(xcor, 240)
        self.write_score()

    def write_score(self):
        self.write(font=FONT, align="center", arg=self.score)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.teleport(0, 0)
        self.write(font=FONT, align="center", arg="Game over")
