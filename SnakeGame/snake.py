from turtle import Turtle

STARTING_X_POSITIONS = [0, -20, -40]
SPEED = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    """Models the snake and its movements."""

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        self.last_segment = self.snake_segments[-1]

    def create_snake(self):
        for position in STARTING_X_POSITIONS:
            self.add_segment(position, 0)

    def add_segment(self, xcor, ycor):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.teleport(xcor, ycor)
        self.snake_segments.append(snake)

    def extend(self):
        self.add_segment(self.last_segment.xcor(), self.last_segment.ycor())

    def reset_snake(self):
        for segment in self.snake_segments:
            segment.teleport(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]
        self.last_segment = self.snake_segments[-1]

    def move(self):
        """Makes the snake move forward."""
        for segment_nr in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment_nr - 1].xcor()
            new_y = self.snake_segments[segment_nr - 1].ycor()
            self.snake_segments[segment_nr].goto(new_x, new_y)
        self.head.forward(SPEED)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
