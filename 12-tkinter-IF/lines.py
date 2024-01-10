import tkinter

width = 600
height = 600
d = 1

x = 0
y1 = 0
color1, color2 = "red", "blue"

canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()


for i in range(width // d):

    canvas.create_line(x+d, 0, x+d, height, width=2, fill=color1)
    color1, color2 = color2, color1
    canvas.create_line(0, y1 + d, width, y1 + d, width=2, fill=color1)
    x += d
    y1 += d

















canvas.mainloop()