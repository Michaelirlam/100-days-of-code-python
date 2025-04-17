from turtle import Turtle

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
        self.snake_body[0].left(90)

    def right(self):
        self.snake_body[0].right(90)

    def move(self):
        for body in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[body].goto(self.snake_body[body - 1].pos())
        self.snake_body[0].forward(20)
    