from tkinter import *
import tkinter.messagebox
import tkinter as tk
from PIL import ImageTk, Image
import calendar
root = Tk()
root.geometry('370x420')
root.title('Calender')
root.config(background="white")
root.resizable(0,0)

def show():
        m = int(month.get())
        y = int(year.get())
        output = calendar.month(y,m)
        cal.config(text=output)

def clear():
        cal.config(text="")

def iexit():
    root.destroy()

#IMAGE
img = ImageTk.PhotoImage(Image.open('calendar.png'))
label = Label(image=img,background="white")
label.place(x=150,y=3)

#MONTH
m_label = Label(root,text="Month",font=('Poppins','15','bold'),background="white")
m_label.place(x=30,y=70)

month = Spinbox(root, from_= 1, to = 12,width="5") 
month.place(x=110,y=80) 

#YEAR  
y_label = Label(root,text="Year",font=('Poppins','15','bold'),background="white")
y_label.place(x=210,y=70)

year = Spinbox(root, from_= 2020, to = 3000,width="8") 
year.place(x=270,y=80) 

cal = Label(root,width=23,height=9,relief=RIDGE,font=("courier",16,"bold"),justify=LEFT,background="white")
cal.place(x=30,y=110)

Button_f = Frame(root,width=23,relief=RIDGE,borderwidth=2)
Button_f.place(x=30,y=322)
show = Button(Button_f,text="Show",font=('Poppins',15,'bold'),relief=RIDGE,borderwidth=2,command=show,padx=14.5)
show.grid(row=0,column=1)

clear = Button(Button_f,text="Clear",font=('Poppins',15,'bold'),relief=RIDGE,borderwidth=2,command=clear,padx=14)
clear.grid(row=0,column=2)

exit_but = Button(Button_f,text="Exit",font=('Poppins',15,'bold'),relief=RIDGE,borderwidth=2,command=iexit,padx=21)
exit_but.grid(row=0,column=3)
root.mainloop()
