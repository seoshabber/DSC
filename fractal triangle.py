from tkinter import *
import time
import random
tk=Tk()
canvas=Canvas(tk, width=500, height=500)
canvas.configure(background = 'light gray')
canvas.pack()
x= 250
y= 250#기준점, 프랙탈 점의 중간점
for i in range(50000):
    dice = random.randint(1,3)
    if dice == 1:
        px = 250
        py = 50
        mycolor='red'
    elif dice == 2:
        px = 50
        py = 450
        mycolor = 'green'
    else:
        px=450
        py=450
        mycolor='blue'

    x=(x+px)/2
    y=(y+py)/2
    canvas.create_line(x,y,x+1,y+1,fill=mycolor)
    tk.update()
    time.sleep(0.005)
