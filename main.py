import time

from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()

lvl = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    player.finish()
    screen.update()
    car_manager.create_car()
    car_manager.car_move(lvl)

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.finish():
        player.go_to_start()
        scoreboard.increase_level()
        lvl += 1


screen.exitonclick()
