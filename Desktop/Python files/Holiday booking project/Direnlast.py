from tkinter import *

window = Tk()

window.geometry("500x300")

window.configure(background = "blue")
window.title("Cruise holidays")

frame = Frame(window)
frame.pack()

titleframe =LabelFrame(frame, text= "--------Welcome to Holiday Cruises UK")
titleframe.grid(row=0, column=1, sticky="w",padx="30",pady = "30")

def myClick():
    noOfPas=no_passengers.get()
    print("Number of passengers is" +noOfPas)
   

def submit():
    selected=no_passengers.get()
    chosen=itinerary.get()
    choice=date_time.get()
   
    print("you chose", selected, "passengers.Your destination is: ", chosen, "and dates are=", choice)
   
def calculate():
 
 
    if  itinerary== optional_destinations[0].get():
        total = 2400 * selected.get()
       
    if itinerary == optional_destinations[1].get():
        total = 3800*selected.get()
       
    if itinerary == optional_destinations[2].get():
        total = 4800*selected.get()
    if itinerary== optional_destinations[3].get():
        total = 2000*selected.get()
   
    if itinerary == optional_destinations[4].get():
        total = 3000* selected.get()

    if itinerary == optional_destinations[5].get():
        total = 3500*nselected.get()

        print(total)


 #4- create the variables

no_passengers=IntVar(window)

itinerary = StringVar(window)

date_time=StringVar(window)




#5.1-create the components

itinerary.set("Select a destination")
date_time.set("Select date")


optional_destinations=["Caribbean- £2400 pp","Australia- £3800pp","Japan- £4800pp","Meditterenian - £2000pp","South Africa- £3000pp","South America- £3500pp"]
choose_date_time=["Jan 15-Feb 15", "March 15- April 15", "May 15- June 15", "July 15- August 15", "September 15- October 15", "November 15- December 15"]

passengers = Label(titleframe, text="Holiday makers").grid(row=1, column = 0, sticky ="w", padx="20")
textbox_1=tkinter.Entry(titleframe, textvariable= no_passengers).grid(row=1, column = 1, sticky ="w", padx="20")
button_1 = tkinter.Button(titleframe, text="Enter no of Passengers", command = myClick).grid(row=5,column=2, sticky="w", padx="20")                           
                       
selected = Entry(titleframe,width= 50).grid(row=1,column=1,sticky="e", padx="20")
destination = Label(titleframe, text="Destination").grid(row=2,column=0,sticky="w", padx="20")
option =OptionMenu(titleframe,itinerary,*optional_destinations).grid(row=2,column=1,sticky="e", padx="20")
dateTime= Label(titleframe, text="Date").grid(row=3,column=0,sticky="w", padx="20")
select=OptionMenu(titleframe,date_time,*choose_date_time).grid(row=3,column=1,sticky="e", padx="20")
                           
submit_button = Button(titleframe, text= "Submit", command=submit).grid(row=4,column=1,sticky="e", padx="35")
calculate_button=Button(titleframe, text="Calculate", command=calculate).grid(row=5, column=1, sticky="e", padx="35")
#e=Entry(window,width= 35, borderwidth=5)
#e.grid(row=5, column=0, columnspan=3, padx=10, pady=10)'''

#myButton = Button(titleframe, text="Enter no of Passengers", command=myClick).grid(row=5,column=2, sticky="w", padx="20")

selected.pack()
option.pack()
select.pack()
submit_button.pack()
calculate_button.pack()
myLabel.pack()

#7-call the mainloop methods on the top container

window.mainloop()
