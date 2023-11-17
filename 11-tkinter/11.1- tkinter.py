import tkinter as tk
import random

x = 10
y = 10
d = 50
w = 1
times = 7

width = d * times + x
height = (d + d // 2) * times + y
count = width // d    # " // " = celociselne delenie 7 // 3 = 2
count2 = height // d
stvrtina = d // 4


canvas = tk.Canvas(width=width, height=height)
canvas.pack()



for i in range(count2):
    for j in range(count):
        canvas.create_rectangle(x,  y+d // 2, x+d, y+(d // 2)+d)
        canvas.create_polygon(x, y+d//2, x+2*stvrtina, y, x+d, y+d//2, outline="black", fill="#f0f0ed")
        canvas.create_rectangle(x+stvrtina, y+d // 2+stvrtina, x+3*stvrtina, y+d // 2+3*stvrtina)
        canvas.create_line(x+stvrtina, y+d // 2+2*stvrtina, x+3*stvrtina,y+d // 2+2*stvrtina)
        canvas.create_line(x+2*stvrtina, y+d // 2+stvrtina, x+2*stvrtina, y+d // 2+3*stvrtina)
        x = x + d
    y = y + d + d // 2
    x = x - d*count


canvas.mainloop()
