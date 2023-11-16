import tkinter as tk
import random

canvas = tk.Canvas(width=600, height=500)
canvas.pack()

x = 10
y = 10
d = 30
w = 1
"""
count = 600 // d    # " // " = celociselne delenie 7 // 3 = 2
count2 = 500 // d

for j in range(count2):
    for i in range(count):
        color = random.choice(("purple2", "purple3", "purple4", "purple1"))
        color2 = random.choice(("orange", "pink", "yellow", "black"))
        canvas.create_rectangle(x, y, x + d, y + d, width=w, fill=color2, outline=color)
        canvas.create_line(x, y, x + d, y + d, width=w, fill=color)
        canvas.create_line(x, y + d, x + d, y, width=w, fill=color)
        x = x + d
    y = y + d
    x = x - d * count
"""
pocet = 598 // d    # // je celociselne delenie 7 // 3 = 2
for j in range(498 // d):
    for i in range(pocet):
        color = random.choice(("green", "red", "blue", "orange", "purple"))
        canvas.create_rectangle(x, y, x+d, y+d, fill = color)
        canvas.create_line(x, y, x+d, y+d)
        canvas.create_line(x, y+d, x+d, y)
        x = x + d  #nakresli stvorcek vedla dalsieho stvorceka
    y = y + d
    x = x-d*pocet
canvas.mainloop()
