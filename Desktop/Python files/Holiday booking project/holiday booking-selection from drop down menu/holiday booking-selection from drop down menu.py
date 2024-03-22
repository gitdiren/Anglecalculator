#1- import the required library or libraries
from tkinter import *

tkinter.messagebox.showinfo("Welcome to Holiday Cruises UK! Please select your holiday options from our drop down menu!")

#2- define the subroutines, function, methods for callback

def submit():
    selected = user_selection.get()
    travellers = no_people.get()
    dates = date_select.get()

def calculate():
    if selected == optional_selection[0]:
        total = 2400*travellers
        
    if selected == optional_selection[1]:
        total = 3800*travellers
       
    if selected == optional_selection[2]:
        total = 4800*travellers
      
    if selected == optional_selection[3]:
        total = 2000*travellers
   
    if selected == optional_selection[4]:
        total = 3000*travellers

    if selected == optional_selection[5]:
        total = 3500*travellers

print(total)
        
   
print("your selected destination is :", selected, "selected no of passengers is :", travellers, "dates selected are: ", dates)


tkinter.messagebox.showinfo("your selected destination is :", selected, "selected no of passengers is :", travellers, "dates selected are: ", dates)

#3-create the top container

window = Tk()
window.title("Holiday Cruises UK")

window.geometry("600x400")

window. configure(background = "green")

frame = Frame(window)
frame.pack()

titleframe =labelFrame(frame, text= "--------Welcome to Holiday Cruises UK")
titleframe.grid(row=0, column=1, sticky="w",padx="30",pady = "30")

#4- create the variables

user_selection = StringVar(window)
no_people = IntVar(window)
date_select = StringVar(window)
varA = StringVar(window)


#5.1-create the components
user_selection.set("Select a destination")
no_people.set("Select no of passengers")
date_select.set("Select date")
optional_destination = ["Caribbean- £2400 pp" , "Australia- £3800pp", "Japan- £4800pp","Meditterenian - £2000pp", "South Africa- £3000pp", "South America- £3500pp"]
optional_date_selection = ["Jan 15-Feb 15" , "March 15- April 15", "May 15- June 15", "July 15- August 15", "September 15- October 15", "November 15- December 15]
optional_passengers = [1,2,3,4,5,6,7,8,9,10]
                           
options = OptionMenu(titleframe,window,user_selection, *optional_selection)
submit_button = Button(window, text= "Submit destination", command = submit)

#6.1- place the component
options.pack()
submit_button.pack()


#7-call the mainloop methods on the top container

window.mainloop()
    
