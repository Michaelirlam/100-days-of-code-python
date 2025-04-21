from turtle import Turtle
import random

# This class is responsible for creating the food for the snake game
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self, snake_positions=None):
        """Refreshes the food position to a random location on the screen"""
        # Generate random coordinates for the food
        # Ensure the food does not spawn on the snake
        while True:
            random_x = random.randint(-280, 280)
            random_y = random.randint(-280, 280)
            if snake_positions:
                if (random_x, random_y) not in snake_positions:
                    break
            else:
                break
        self.goto(random_x, random_y)
