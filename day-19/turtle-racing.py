from turtle import Turtle, Screen
import random

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

turtles = [leonardo, donatello, michelangelo, raphael, davinci, vangogh]
turtle_colour = ["blue", "purple", "orange", "red", "green", "pink"]

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




# Screen settings
screen = Screen()
screen.setup(height=400, width=500)


# Game logic

is_race_on = False

draw_finish_line()
starting_pos()

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a colour: ")

if user_bet:
    is_race_on = True

while is_race_on:
    move = random.randint(0, 10)
    random.choice(turtles).forward(move)
    
    for t in turtles:
        if t.xcor() >= 230:
            is_race_on = False
            if user_bet == turtle_colour[turtles.index(t)]:
                print("You Won")
            else:
                print(f"you Lost, the winner is {turtle_colour[turtles.index(t)]}")

screen.exitonclick()