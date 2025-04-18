from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.pencolor("white")
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial",16, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

        
        
        
