from turtle import Turtle
import random

COLOURS = ["red", "blue", "yellow", "orange", "green", "pink", "purple"]

class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = 1
        
    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.turtlesize(2,3)
        new_car.color(random.choice(COLOURS))
        new_car.penup()
        new_car.hideturtle()
        new_car.goto(300, random.randint(-240, 240))
        new_car.showturtle()
        self.cars.append(new_car) 
    
    def move_car(self, car):
        car.setx(car.xcor() - self.speed)
    
    def increase_speed(self):
        self.speed *= 1.1