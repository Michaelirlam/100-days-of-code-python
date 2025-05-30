from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.score = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="left", font=("Arial", 16, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER!", move=False, align="center", font=("Arial", 16, "normal"))
    
