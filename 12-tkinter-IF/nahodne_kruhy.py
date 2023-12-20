import tkinter, random

width = 500
height = 500
d = 20

canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()

for i in range(2000):
    x = random.randint(2, width-d-2)
    y = random.randint(2, height-d-2)

    if x <= (width//2) and y <= (height//2):
        color = "orange"
    elif x <= (width//2) and y >= (height//2):
        color = "blue"
    elif x >= (width//2) and y <= (height//2):
        color = "green"
    elif x >= (width//2) and y >= (height//2):
        color = "purple"

    canvas.create_oval(x, y, x+d, y+d, fill=color)



#char






canvas.mainloop()