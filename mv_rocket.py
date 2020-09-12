import time
from tkinter import *

tk=Tk()
canvas = Canvas(tk, width=500, height = 500)
canvas.pack()

canvas.create_polygon(225,440,275,440,250,400)
canvas.create_rectangle(225,440,275,490,fill="black")


while True:
    for i in range(78):
        canvas.move(1, 0, -5)
        canvas.move(2, 0, -5)
        tk.update()
        time.sleep(0.0205)
    for i in range(130):
        canvas.move(1,0,3)
        canvas.move(2,0,3)
        tk.update()
        time.sleep(0.05)
