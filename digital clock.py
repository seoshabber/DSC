from tkinter import *
import time

tk = Tk()
canvas = Canvas(tk, width = 500, height = 500)
canvas.pack()
width = 500
height = 500    #왜 width와 height를 넣는건지?

while 1:
    t=time.localtime()
    hour = t[3]
    min = t[4]
    sec = t[5]
    canvas.delete("all")
    myclock = str(hour) + ':'+ str(min)+':'+str(sec)
    canvas.create_text(250, 250, text = myclock, font=('Arial',25))
    tk.update()
    time.sleep(1)
