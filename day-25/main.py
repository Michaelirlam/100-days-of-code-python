# Importing the required libraries
import turtle as t
import pandas

# This program is a game where the user has to guess the names of all 50 US states.
# The user is prompted to enter a state name, and if it is correct, the state is marked on a map.
# The program uses the turtle graphics library to display the map and the guessed states.
# The user can keep guessing until they have named all 50 states, at which point a congratulatory message is displayed.

image = "./blank_states_img.gif"

# Setting up the screen and turtle graphics
screen = t.Screen()
screen.title("U.S. States Game")
screen.addshape(image)

# Setting the turtle shape to the image of the US map
t.shape(image)

# Setting up the turtle to write the guessed states on the map
writer = t.Turtle()
writer.penup()
writer.hideturtle()

# Reading the CSV file containing the states and their coordinates
data = pandas.read_csv("./50_states.csv")
# The CSV file contains the names of the states and their x, y coordinates on the map
states = data.state.to_list()

# The list of states is used to check if the user's guess is correct 
# and a counter is initialized to keep track of the number of correct guesses
count = 0
guessed = []

# The game loop continues until the user has guessed all 50 states
while True:
    # The user is prompted to enter a state name
    guess = screen.textinput(title=f"{count}/50 States Guessed.", prompt="Name a US State:")

    guess = guess.title()

    if guess == "Exit":
        # If the user types "Exit", the program will save the states that were not guessed to a CSV file
        missing_states = [state for state in states if state not in guessed]
        missing_data = pandas.DataFrame(missing_states)
        missing_data.to_csv("missing_states.csv")
        break

    # Checking if the guess is correct
    if guess in states:
        if guess not in guessed:
            guess_row = data[data.state == guess]
            writer.goto(x=int(guess_row.x), y=int(guess_row.y))
            writer.write(f"{guess}", move=False, align="center", font=("Arial", 8, "normal"))
            count += 1
            guessed.append(guess)

    # Checks if win condition is met
    if len(guessed) == 50:
        writer.goto(0, 0)
        writer.color("green")
        writer.write("You Win!", move=False, align="left", font=("Arial", 30, "bold"))
        break

    
t.mainloop()
