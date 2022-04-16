from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
window = Tk()
window.title("Color")
window.geometry("500x500")
window.config(bg="lavender")
messagebox.showinfo("Meassage","This is a demo of this App please dont Share this App")

def click():
    color=colorchooser.askcolor()
    colorHex=color[1]
    window.config(bg=colorHex)
    button1.pack(anchor=CENTER)
    la2=Label(window,text="Your Color Code:",font=("Lalezar",35),bg=colorHex)
    la2.place(x=10,y=250)

    co=Label(window,text=colorHex,font=("Lalezar",40),bg=colorHex)
    co.place(x=300,y=250)





button1=Button(window,text="Choose a color",font=("",40),command=click,bg="lavender")
button1.pack(anchor=CENTER)



window.mainloop()