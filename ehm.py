import tkinter as Tk
from random import randrange

width = 450
canvas = Tk.Canvas(width=width)
canvas.pack()

def main():
    stvorce2('40 red 20 blue 60 purple 40 red 30 gold')


def stvorce(vel, retazec):
    x = y = 30
    retazec += " "
    for i in range(retazec.count(" ")):
        kde = retazec.find(" ")
        color = retazec[:kde]
        retazec = retazec[kde+1:]
        canvas.create_rectangle(x, y, x+vel, y+vel, fill=color)
        x += vel+5

def stvorce2(retazec):
    x, y = 10, 200
    retazec = retazec1 = retazec+" "
    while True:
        if retazec == "":
            retazec = retazec1
        elif x > width:
            break
        kde = retazec.find(" ")
        size = int(retazec[:kde])
        retazec = retazec[kde+1:]
        kde = retazec.find(" ")
        color = retazec[:kde]
        retazec = retazec[kde+1:]
        if x+size+5 > width:
            break
        canvas.create_rectangle(x, y, x+size, y-size, fill=color)
        x += size + 5

def hmm():
    for i in range(5):
        x = y = 50
        color = f"#{randrange(256**3):06x}"
        canvas.create_text(x+50*i, y, text=chr(int(0x2654) + 1*i), font='arial 50', fill=color)

def kresli(retazec):
    x, y = 100, 100
    for znak in retazec:
        x1, y1 = x, y
        if znak == 's':
            y1 -= 10
        elif znak == 'v':
            x1 += 10
        elif znak == 'j':
            y1 += 10
        elif znak == 'z':
            x1 -= 1
        else:
            break
        canvas.create_line(x, y, x1, y1)
        x, y = x1, y1


main()
canvas.mainloop()
