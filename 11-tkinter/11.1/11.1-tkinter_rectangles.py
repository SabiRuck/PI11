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
        r = random.randrange(256)
        g = random.randrange(256)
        b = random.randrange(256)
        color = f'#{r:02x}{g:02x}{b:02x}'
        color2 = "black"
        canvas.create_rectangle(x, y, x + d, y + d, width=w, fill=color2, outline=color)
        canvas.create_line(x, y, x + d, y + d, width=w, fill=color)
        canvas.create_line(x, y + d, x + d, y, width=w, fill=color)
        x = x + d
    y = y + d
    x = x - d * count

canvas.mainloop()