from turtle import Turtle
FONT = ("Courier", 18, "normal")


def read_score():
    with open("highscore.txt") as file:
        return file.read()


def update_highscore(score):
    with open("highscore.txt", mode="w") as file:
        file.write(f"{score}")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.teleport(0, 260)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(font=FONT, align="center", arg=f"Score: {self.score} Highscore: {read_score()}")

    def update_score(self):
        self.score += 1
        self.write_score()

    def reset_game(self):
        if self.score > int(read_score()):
            update_highscore(self.score)
        self.score = 0
        self.write_score()
