from turtle import Turtle

MOVE_DISTANCE = 20

class Snake():

    def __init__(self):
        self.snake_body = []
        for num in range(3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.setpos(x= -20 * num, y=0)
            self.snake_body.append(new_segment)
    
    def left(self):
        """Moves snake left when assigned to an onkey, stops snake from moving into itself"""
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def right(self):
        """Moves snake right when assigned to an onkey, stops snake from moving into itself"""
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)
    
    def up(self):
        """Moves snake up when assigned to an onkey, stops snake from moving into itself"""
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)
    
    def down(self):
        """Moves snake down when assigned to an onkey, stops snake from moving into itself"""
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def move(self):
        """Makes the snake move forward in the direction its facing"""
        for body in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[body].goto(self.snake_body[body - 1].pos())
        self.snake_body[0].forward(MOVE_DISTANCE)

    def grow(self):
        """Logic to grow the snake"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos((self.snake_body[-1].xcor(), self.snake_body[-1].ycor()))
        self.snake_body.append(new_segment)

    