from tkinter import *
import tkinter.messagebox as box
window = Tk()

window.geometry("700x300")

window.configure(background = "light blue")
window.title("Cruise holidays")

frame = Frame(window)
frame.pack()

titleframe =LabelFrame(frame, text= "--------Welcome to Holiday Cruises UK")
titleframe.grid(row=0, column=1, sticky="w",padx="30",pady = "30")


def myClick():
    noOfPas= no_passengers.get()
    print("Number of passengers is: " + str(noOfPas))
   

#def submit():
    #selected=no_passengers.get()
   # chosen=itinerary.get()
    #choice=date_time.get()
   
    #print("you chose", selected, "passengers.Your destination is: ", chosen, "and dates are=", choice)
   
def calculate():
 
 
    if  itinerary.get() == optional_destinations[0]:
        total = 2400 * no_passengers.get()
       
    if itinerary.get() == optional_destinations[1]:
       total = 3800*no_passengers.get()
       
    if itinerary.get() == optional_destinations[2]:
       total = 4800*no_passengers.get()
    if itinerary.get()== optional_destinations[3]:
       total = 2000*no_passengers.get()
   
    if itinerary.get() == optional_destinations[4]:
       total = 3000*no_passengers.get()

    if itinerary.get() == optional_destinations[5]:
       total = 3500*no_passengers.get()

    print(total)
    box.showinfo("Booking is completed!Total is: ", total)



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

selected = Entry(titleframe,textvariable= no_passengers ).grid(row=1,column=1,sticky="e", padx="20") 

destination = Label(titleframe, text="Destination").grid(row=2,column=0,sticky="w", padx="20")
option =OptionMenu(titleframe,itinerary,*optional_destinations).grid(row=2,column=1,sticky="e", padx="20")
dateTime= Label(titleframe, text="Date").grid(row=3,column=0,sticky="w", padx="20")
select=OptionMenu(titleframe,date_time,*choose_date_time).grid(row=3,column=1,sticky="e", padx="20")
                           
#submit_button = Button(titleframe, text= "Submit", command=submit).grid(row=4,column=1,sticky="e", padx="35")
calculate_button=Button(titleframe, text="Calculate", command=calculate).grid(row=5, column=1, sticky="e", padx="35")
#button_1 = Button(titleframe, text="Enter no of Passengers", command = myClick).grid(row=1,column=3, sticky="w", padx="20")             



#7-call the mainloop methods on the top container

window.mainloop()
