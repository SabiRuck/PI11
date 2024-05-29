import tkinter as Tk

canvas = Tk.Canvas(height=500, width=500)
canvas.pack()

file = open("body.txt", 'r', encoding="utf-8")

for coords in file:
    x, y = coords.split(" ")
    x, y = int(x), int(y)
    canvas.create_oval(x, y, x+20, y+20)
















canvas.mainloop()