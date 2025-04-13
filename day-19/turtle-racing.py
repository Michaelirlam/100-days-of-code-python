from turtle import Turtle, Screen


# Turtle objects for the race and their states
leonardo = Turtle()
leonardo.shape("turtle")
leonardo.color("blue")
leonardo.penup()

donatello = Turtle()
donatello.shape("turtle")
donatello.color("purple")
donatello.penup()

michelangelo = Turtle()
michelangelo.shape("turtle")
michelangelo.color("orange")
michelangelo.penup()

raphael = Turtle()
raphael.shape("turtle")
raphael.color("red")
raphael.penup()

davinci = Turtle()
davinci.shape("turtle")
davinci.color("green")
davinci.penup()

vangogh = Turtle()
vangogh.shape("turtle")
vangogh.color("pink")
vangogh.penup()

# Logic for drawing the finish line and getting the turtles into their starting position

def draw_finish_line():
    raphael.setpos(230, 180)
    raphael.pendown()
    raphael.setpos(230, -180)
    raphael.penup()

def starting_pos():
    leonardo.setpos(-230, 140)
    donatello.setpos(-230, 80)
    michelangelo.setpos(-230, 20)
    raphael.setpos(-230, -40)
    davinci.setpos(-230, -100)
    vangogh.setpos(-230, -160)

draw_finish_line()
starting_pos()


# Screen settings
screen = Screen()
screen.setup(height=400, width=500)

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a colour: ")



screen.exitonclick()