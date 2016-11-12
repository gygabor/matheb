from tkinter import *
import time
import random

root = Tk()
size = 800

canvas = Canvas(root, width=size, height=size)
canvas.pack()

ratio = 3**0.5

def random_color():
    these = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

    fff = []
    for z in range(6):
        fff.append(these[random.randint(0,15)])
        ccc = ''.join(fff)

    return '#' + ccc

def creating_triangle(x, y, a):
    canvas.create_polygon(x, y, x+a, y, x+(a/2), y+(ratio/2)*a, fill=random_color(), outline='black')

def triangles(x, y, a, n):
        time.sleep(0.03)
        creating_triangle(x, y, a)
        canvas.update()
        if n > 0:
            triangles(x, y, a/2, n-1)
            triangles(x+(a/2), y, a/2, n-1)
            triangles(x+(a/4), y+(ratio/2)*a/2, a/2, n-1)




triangles(50, 20, 600, 6)
#creating_triangle(100, 150, 200)

root.mainloop()
