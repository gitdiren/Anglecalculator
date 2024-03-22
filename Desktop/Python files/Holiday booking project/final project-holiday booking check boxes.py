#1- import the required library or libraries
import tkinter as tk 


#3-create main window
root = tk.Tk()
root.geometry("400x300")

#create a frame to contain the widgets
frame0 = tk.Frame(root)
frame0.pack()

#create a widget within the frame

widget1 =tk.Label(frame0, text="first destination")
widget1.grid(row=0, column=0)
caribbean_label = tk.Checkbutton(frame0,text ="Caribbean").grid(row=1,column=0)

#create another widget within the frame

widget2 = tk.Label(frame0, text="second destination")
widget2.grid(row=0, column=1)
australia_label = tk.Checkbutton(frame0,text ="Australia").grid(row=1,column=1)

 
#7-call the mainloop methods on the top container

root.mainloop()
    
