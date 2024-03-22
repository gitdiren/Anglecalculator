import tkinter

def enter():
    fullname = name.get() + " " + surname.get()
    print(fullname)
  

window = tkinter.Tk()

window.geometry("400x400")
window.configure(background= "purple")

name = tkinter.StringVar(window)
surname = tkinter.StringVar(window)

textbox1 =tkinter.Entry(window, textvariable = name).grid(row=1,sticky='e',padx=20,pady=20)
textbox2 =tkinter.Entry(window, textvariable = surname).grid(row=2,sticky='e',padx=20,pady=20)
button = tkinter.Button(window, text ='Enter', command = enter, width=5). grid(row=3,padx=10,pady=10)

window.mainloop()
