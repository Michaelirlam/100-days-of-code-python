from turtle import Turtle

class Scoreboard(Turtle):
    """Scoreboard class to display the scores of the players."""
    def __init__(self):
        super().__init__()
        self.color("White")
        self.player_score = 0
        self.computer_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score() # Call to initialise the scoreboard display
        
    def update_score(self):
        """Updates the scoreboard with the current scores."""
        self.clear()
        self.write(f"{self.player_score} | {self.computer_score}", move=False, align="center", font=("Arial",30, "bold"))
    
    def increase_player_score(self):
        """Increases the player's score by 1."""
        self.player_score += 1
        self.update_score()
    
    def increase_computer_score(self):
        """Increases the computer's score by 1."""
        self.computer_score += 1
        self.update_score()

    def player_win(self):
        """Displays a win message for the player."""
        self.goto(0, 0)
        self.color("red")
        self.write("You Win!", move=False, align="center", font=("Arial", 30, "bold"))
    
    def player_lose(self):
        """Displays a lose message for the player."""
        self.goto(0, 0)
        self.color("red")
        self.write("You Lose!", move=False, align="center", font=("Arial", 30, "bold"))
