from tkinter import *
import math
import datetime


def x_cod(length, angle):
    return width /2 + length* math.cos(angle * math.pi / 180)

def y_cod(length, angle):
    return height /2 -  length * math.sin(angle * math.pi/ 180)

width = 400
height = 400
radius = 150

root = Tk()
root.title("clock")

canvas = Canvas(root, width = width, height = height)
canvas.pack()

canvas.create_oval(width/2-radius, height/2-radius, width/2+radius, height/2+radius) 
seconds = canvas.create_line(0,0,0,0,fill="blue")
minutes = canvas.create_line(0,0,0,0)
hours = canvas.create_line(0,0,0,0)

def change_hand(length, time, clock_hard, degree):
    alpha= 90 - time * degree
    x1 = x_cod(0, alpha)
    y1 = y_cod(0, alpha)
    x2 = x_cod(length, alpha)
    y2 = y_cod(length, alpha)
    canvas.coords(clock_hard, x1, y1, x2, y2)


def update():
    timem = str(datetime.datetime.now())
    se = int(timem[17:19])
    mi = int(timem[14:16])
    ho = int(timem[11:13])

    change_hand(radius - 30, se, seconds,6)
    change_hand(radius - 40, mi, minutes,6)
    change_hand(radius / 2, ho, hours,30)

    root.after(1000,update)


alpha = 60

for i in range(1, 13):
    canvas.create_text(x_cod(radius + 20 , alpha), y_cod(radius + 20 ,alpha),text=i,
     fill="darkred", font="George")
    alpha = alpha - 30

for i in range(60):


    x1 = x_cod(radius, alpha)
    y1 = y_cod(radius, alpha)

    if alpha % 30 == 0:
        x2  = x_cod(radius - 30, alpha)
        y2 = y_cod(radius - 30, alpha)
    else:
        x2  = x_cod(radius - 10, alpha)
        y2 = y_cod(radius - 10, alpha)    
    canvas.create_line(x1, y1,x2, y2)
    alpha += 6 

update()
    
root.mainloop()