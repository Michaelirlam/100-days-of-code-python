from turtle import Screen
from player import Player
from cars import CarManager
from scoreboard import Scoreboard
import time
import random

game_over = False
screen = Screen()
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.title("Turtle Crossing")
screen.setup(600, 600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move, "Up")


def create_car():
    car_manager.create_car()
    screen.ontimer(create_car,800)

def game_loop():
    global game_over

    for car in car_manager.cars:
        car_manager.move_car(car)

        if car.xcor() < -350:
            car_manager.cars.remove(car)
        
        if player.detect_collision(car):
            scoreboard.game_over()
            game_over = True

    if player.finish_line():
        scoreboard.increase_score()
        car_manager.increase_speed()
    
    
    if not game_over:
        screen.ontimer(game_loop, 16)
        screen.update()
    

create_car()
game_loop()
screen.exitonclick()

