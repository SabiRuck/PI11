import tkinter as tk
import random

x = 10
y = 10
d = 30
w = 1
times = 25
times2 = 15

width = d * times + x
height = d * times2 + y
count = width // d    # " // " = celociselne delenie 7 // 3 = 2
count2 = height // d


canvas = tk.Canvas(width=width, height=height)
canvas.pack()


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

canvas.mainloop()