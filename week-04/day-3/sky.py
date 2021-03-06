# create a 300x300 canvas.
# make it look like a nigth sky:
# - The background should be black
# - The stars can be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

from tkinter import *
import random
import time

root = Tk()

w = 300
h = 300

canvas = Canvas(root, width=w, height=h, bg="black")
canvas.pack()

def night_sky(n): #the function only needs the number of stars on the dark sky

    for i in range(n):
        a = random.randint(1, 3)
        b = a
        RR=("%02x"%random.randint(200,255))
        GG=("%02x"%random.randint(180,255))
        BB=("%02x"%random.randint(200,255))
        ge="#"
        color=ge+RR+GG+BB
        x = random.randint(0, w)
        y = random.randint(0, h)
        time.sleep(0.05)
        canvas.create_polygon(x, y, x+a, y, x+a, y+b, x, y+b, fill=color)
        canvas.update()

night_sky(30)

root.mainloop()
