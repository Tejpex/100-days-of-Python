from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.teleport(-260, 240)
        self.write_level()

    def write_level(self):
        self.write(font=FONT, align="left", arg=f"Level: {self.level}")

    def update_level(self):
        self.level += 1
        self.clear()
        self.write_level()

    def game_over(self):
        self.teleport(0, 0)
        self.write(font=FONT, align="center", arg="GAME OVER")
