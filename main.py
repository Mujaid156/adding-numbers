import tkinter
from tkinter import *

window = Tk()
window.geometry("500x500")  # size of window

# name of application
window.title("Adding two numbers")


# allows
num1 = StringVar()
num2 = StringVar()
result = StringVar()

def adding_inputs():
    one = float(first_number.get())
    two = float(second_number.get())
    ans = one + two
    return result.set(ans)

def clear_inputs():
    first_number.delete(0, END)
    second_number.delete(0, END)
    answer.config(state="normal")
    answer.delete(0, END)
    answer.config(state="readonly")

def exit_program():
    return window.destroy()

# display text
label_first_number=Label(window, text="First number")
label_second_number=Label(window, text="Second number")
label_answer=Label(window, text="Answer")

# entry text
first_number=Entry(window, textvariable = num1)
second_number=Entry(window, textvariable = num2)
answer=Entry(window, textvariable = result, state = DISABLED)

# adds buttons
add=tkinter.Button(window, text = "Add", command = adding_inputs)
clear=tkinter.Button(window, text = "Clear", command = clear_inputs)
exit=tkinter.Button(window, text = "Exit", command = exit_program)


# placing labels
label_first_number.place(x=0, y=0)
label_second_number.place(x=0, y=30)
label_answer.place(x=0, y=60)

# placing entry
first_number.place(x=125, y=0)
second_number.place(x=125, y=30)
answer.place(x=125, y=60)

# placing buttons
add.place(x=75, y=100)
clear.place(x=135, y=100)
exit.place(x=205, y=100)

# runs program all the time
window.mainloop()
