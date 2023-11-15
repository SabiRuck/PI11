import tkinter as tk
import random

canvas = tk.Canvas(width=600, height=500)
canvas.pack()

x = 100
y = 100
d = 100
w = 1
count = 600 // d    # " // " = celociselne delenie 7 // 3 = 2
count2 = 500 // d
"""
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
stvrtina = d // 4

#canvas.create_rectangle(x,  y+d // 2, x+d, y+(d // 2)+d)
#canvas.create_polygon(x + d // 2, y, x+d, x+d, y+(d // 2)+d, x + d // 2, y)
canvas.create_rectangle(x+stvrtina, y+d // 2+stvrtina, x+3*stvrtina, y+d // 2+3*stvrtina)
#canvas.create_line(x+stvrtina, y+d // 2+2*stvrtina, x+3*stvrtina,y+d // 2+2*stvrtina)
#canvas.create_line()







canvas.mainloop()
