#1- import the required library or libraries
from tkinter import *

#2- define the subroutines, function, methods for callback

def submit():
    selected = user_selection.get()
    print(selected)
    total = 0
    if selected == optional_selection[0]:
        total = total + 2400
        print("destination cost per person is: ", total)
    if selected == optional_selection[1]:
        total = total + 3800
        print("destination cost per person is: ", total)
    if selected == optional_selection[2]:
        total = total + 4800
        print("destination cost per person is: ", total)
    if selected == optional_selection[3]:
        total = total + 200
        print("destination cost per person is: ", total)
    if selected == optional_selection[4]:
        total = total + 3000
        print("destination cost per person is: ", total)
    if selected == optional_selection[5]:
        total = total + 3500
        print("destination cost per person is: ", total)



#3-create the top container

window = Tk()
window.geometry("400x300")

#4- create the variables

user_selection = StringVar(window)



#5.1-create the components
user_selection.set("Select a destination")
optional_selection = ["Caribbean- £2400" , "Australia- £3800", "Japan- £4800","Meditterenian - £2000", "South Africa- £3000", "South America- £3500"]

options = OptionMenu(window,user_selection, *optional_selection)
submit_button = Button(window, text= "Submit destination", command = submit)

#6.1- place the component
options.pack()
submit_button.pack()


#7-call the mainloop methods on the top container

window.mainloop()
    
