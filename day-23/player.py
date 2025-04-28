from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.turtlesize(1.5, 1.5)
        self.penup()
        self.setheading(90)
        self.teleport(0, -270)

    def move(self):
        self.sety(self.ycor() + 60)
    
    def finish_line(self):
        if self.ycor() >= 270:
            self.teleport(0, -270)
            return True
    
    def detect_collision(self, car):
        return self.distance(car) < 30