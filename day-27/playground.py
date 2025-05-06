import tkinter

window = tkinter.Tk()
window.title("GUI")
window.minsize(500, 400)


my_label = tkinter.Label(text="...", font=("Arial", 16, "bold"))
my_label.grid(column=0, row=0)

def button_clicked():
    my_label.config(text=input.get())

button = tkinter.Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

button_two = tkinter.Button(text="I'm a new button")
button_two.grid(column=2, row=0)

input = tkinter.Entry(textvariable=my_label)
input.grid(column=3, row=2)

    


window.mainloop()