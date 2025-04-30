from turtle import Turtle

# This class is responsible for creating the scoreboard for the snake game
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.pencolor("white")
        self.update_score()
        
    def update_score(self):
        """Updates the score on the screen"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Arial",16, "bold"))

    def increase_score(self):
        """Increases the score by 1"""
        self.score += 1
        self.update_score()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0

"""
    def game_over(self):
        Displays game over message
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER!", move=False, align="center", font=("Arial", 24, "bold"))"""

    