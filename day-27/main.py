import tkinter

window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(200, 100)
window.config(padx=100, pady=100)

# Interactivity

def button_clicked():
    """Takes user input in form of an int and calculates the conversion to Km"""
    sum = int(input.get()) * 1.609 
    result.config(text=str(sum))

# Labels
miles_label = tkinter.Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)

km_label = tkinter.Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

result = tkinter.Label(text="0", font=("Arial", 12, "bold"))
result.grid(column=1, row=1)

is_equal_to = tkinter.Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_to.grid(column=0, row=1)


# Buttons

calculate_button = tkinter.Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

# Inputs

input = tkinter.Entry(textvariable=result)
input.grid(column=1, row=0)


window.mainloop()
