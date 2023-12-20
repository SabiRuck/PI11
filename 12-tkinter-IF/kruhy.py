import tkinter

width = 200
height = width
d = 15

canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()

n = width//d
s = n // 2

for i in range(n):  #riadky
    for j in range(n):  #stlpce
        if j == s or i == s:
            color = "red"
        else:
            color = "white"

        x = j * d + 2
        y = i * d + 2
        canvas.create_oval(x, y, x+d, y+d, fill=color)







canvas.mainloop()