from turtle import Turtle

class Ball(Turtle):
    """Ball class to create a ball for the pong game."""
    def __init__(self, shape = "circle"):
        super().__init__(shape)
        self.color("white")
        self.penup()
        self.x_move = 10 # Horizontal speed of the ball 
        self.y_move = 5 # Vertical speed of the ball

    def move(self):
        """Moves the ball in the current direction."""
        new_x = self.xcor() + self.x_move # Move the ball horizontally (by 10 pixels)
        new_y = self.ycor() + self.y_move # Move the ball vertically (by 5 pixels)
        self.goto(new_x, new_y)
    
    def bounce_x(self):
        """Reverses the ball's horizontal direction."""
        self.x_move *= -1

    def bounce_y(self):
        """Reverses the ball's vertical direction"""
        self.y_move *= -1    
    
    def reset_position(self):
        """Reset the ball to the center and reverse its direction."""
        self.teleport(0, 0) # Reset position to center, used over goto to avoid flickering
        self.bounce_x()  # Reverse direction to give the other player a chance

    