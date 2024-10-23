import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.go_up, "Up")

car_manager = CarManager()
scoreboard = Scoreboard()

# Wait-time between new cars
wait_time_low = 5
wait_time_high = 15

game_is_on = True
while game_is_on:
    for _ in range(random.randint(wait_time_low, wait_time_high)):
        car_manager.move()

        # Detect collision with cars
        for car in car_manager.cars:
            if player.distance(car) < 27:
                game_is_on = False
                scoreboard.game_over()

        # Detect when player gets to the top
        if player.is_at_finish_line():
            player.restart()
            scoreboard.update_level()
            car_manager.increase_speed()
            if wait_time_low > 0:
                wait_time_low -= 1
            if wait_time_high > 3:
                wait_time_high -= 3

        time.sleep(0.1)
        screen.update()

    # At random times add a new car
    car_manager.add_car()

screen.exitonclick()
