import mysql.connector
from tkinter import *
import Task

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Saikumar123$",
)

def submit():
    type=Coffee.get()
    obj=Task.CoffeeMaker()
    money=m.get()
    can(root,obj.start(type,float(money)))

def can(root,tex):
    Message(root,text=tex).place(x=80,y=160)

root = Tk()
root.geometry("300x300")
root.title("CoffeeMaker")
C = Canvas(root, bg ="blue", height = 250, width = 300)
lblfrstrow = Label(root, text ="Which coffee do you need")
lblfrstrow.place(x = 50, y = 20)
Coffee=Entry(root)
Coffee.place(x=70,y=40)
lblfrstrow = Label(root, text ="Enter Money")
lblfrstrow.place(x = 50, y = 60)
m=Entry(root)
m.place(x=70,y=80)
submitbtn = Button(root, text ="Ok",
                      bg ='blue', command = submit)
submitbtn.place(x = 100, y = 135, width = 55)
root.mainloop()
