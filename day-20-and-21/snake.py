from turtle import Turtle

MOVE_DISTANCE = 20 # The distance the snake moves each time

# This class is responsible for creating the snake
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

    def detect_wall_collision(self, boundary=290):
        """
        Checks if the snake has hit the wall
        :param boundary: The distance from the center of the screen to the wall
        :return: True if the snake has hit the wall, False otherwise
        """
        head = self.snake_body[0]
        return head.xcor() > boundary or head.xcor() < -boundary or head.ycor() > boundary or head.ycor() < -boundary
    
    def detect_tail_collision(self):
        """Checks if the snake has hit its own tail"""
        # Check if the head is too close to any of the body segments
        head = self.snake_body[0]
        for segment in self.snake_body[1:]:
            if head.distance(segment) < 10:
                return True
        return False
    
    def wall_teleport(self, boundary=300):
        head = self.snake_body[0]
        if head.xcor() > boundary:
            head.goto(x=-boundary, y=head.ycor())
        elif head.xcor() < -boundary:
            head.goto(x=boundary, y=head.ycor())
        elif head.ycor() > boundary: 
            head.goto(x=head.xcor(), y=-boundary)
        elif head.ycor() < -boundary:
            head.goto(x=head.xcor(), y=boundary)
            

    

    