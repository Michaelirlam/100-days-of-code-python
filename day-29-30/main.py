from tkinter import *
from tkinter import messagebox
from password import Password
import json

WHITE = "#ffffff"

#TODO: Logic and graphics for checking password is weak, medium, strong
#TODO: Add show checkbox and logic to reveal password

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

password_generator = Password()

# Generated random password when generate password button is pressed
def generate_password():
    generate = password_generator.generate(nr_letters=10, nr_symbols=4, nr_numbers=4)
    password_variable.set(generate)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    """Function to save password to JSON file"""
    #TODO: Add check to make sure password meets criteria
    
    # Gets the input for website, email, password
    website = website_variable.get()
    email = email_username_variable.get()
    password = password_variable.get()
    data_dict = {website: {
        "email": email,
        "password": password,
    }}

    #Check to make sure no fields are blank
    if not website or not email or not password:
        messagebox.showwarning(title="Warning!", message="Please fill out all fields!")
    else:
        # Asks user if they want to save and returns a bool: yes = True, no = False
        is_ok = messagebox.askyesno(message=f"You are about to save:\nemail: {email}\npassword: {password}\nAre you sure you want to save?")
        if is_ok:
            # Try/catch to see if existing JSON file and writes email and password to file
            try:
                # Checks to see if we can open the file
                with open("./passwords.json", "r") as file:
                    # Read JSON data
                    data = json.load(file)
                    # Update old data with new data
                    data.update(data_dict)
            except (FileNotFoundError, json.JSONDecodeError):
                # If no file exists changes data to equal data dictionary so it can be written to JSON
                data = data_dict

            with open("./passwords.json", "w") as file:
                # save updated data
                json.dump(data, file, indent=4)

            messagebox.showinfo(title="Success!", message="Password save successful!")
        
            # Reset website and password inputs to be blank
            website_variable.set("")
            password_variable.set("")

#----------------------------- SEARCH -------------------------------------#

def search():
    """Function to search for existing passwords in the password manager"""
    website = website_variable.get()
    try:
        with open("./passwords.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showwarning(title="Error", message="No data file found or file is corrupted.")
        return
    else:
        if website in data:
            email = data[website]["email"]
            password =  data[website]["password"]
            messagebox.showinfo(title=website, message=f"email: {email}\npassword: {password}")
        else:
            messagebox.showwarning(title="Not found", message=f"No details for '{website}' found.")

# ---------------------------- UI SETUP ------------------------------- #

# Screen setup
window = Tk()
window.title("MyPass: Password Manager")
window.config(padx=20, pady=20, background=WHITE)

# Logo canvas setup
my_pass_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0, background=WHITE)
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(column=0,row=0, columnspan=3)

# Website/URL label and input setup
website_label = Label(text="Website/URL:", background=WHITE, pady=5)
website_variable = StringVar()
website_input = Entry(width=21, textvariable=website_variable)
website_input.focus()
website_label.grid(column=0, row=1, sticky="e", padx=5)
website_input.grid(column=1, row=1, columnspan=2, sticky="w", padx=5)

# Email/Username label and input setup
email_username_label = Label(text="Email/Username:", background=WHITE, pady=5)
email_username_variable = StringVar()
email_username_input = Entry(width=42, textvariable=email_username_variable)
email_username_input.insert(0, "michaelirlam@hotmail.co.uk")
email_username_label.grid(column=0, row=2, sticky="e", padx=5)
email_username_input.grid(column=1, row=2, columnspan=2, sticky="w", padx=5)

# Password labels, input, and button setup
password_label = Label(text="Password:", background=WHITE, pady=5)
password_variable = StringVar()
password_input = Entry(width=21, textvariable=password_variable, show="*")
generate_password_button = Button(text="Generate Password", command=generate_password)
password_label.grid(column=0, row=3, sticky="e", padx=5)
password_input.grid(column=1, row=3, sticky="w", padx=5)
generate_password_button.grid(column=2, row=3, sticky="w", padx=5)

# Add button setup
add_button = Button(text="Add", width=39, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="w", pady=10, padx=5)

# Search button setup
search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1, sticky="w", padx=5)


# Function to keep window open
window.mainloop()

