import tkinter as tk

x = 5
y = 5
d = 10
times = 2
times2 = 3
color = "black"
color2 = "#590E8C"

width = times * (34 * d) + x
height = times2 * (8 * d) + 2 * y

canvas = tk.Canvas(width=width, height=height, bg="#9e79b3")
canvas.pack()

print(width, height)

for i in range(times2):
    for j in range(times):
        # S
        canvas.create_rectangle(x + d, y + d, x + 2 * d, y + 2 * d, fill=color)
        canvas.create_rectangle(x + 2 * d, y + d, x + 3 * d, y + 2 * d, fill=color2)
        canvas.create_rectangle(x + 3 * d, y + d, x + 4 * d, y + 2 * d, fill=color)
        canvas.create_rectangle(x + 4 * d, y + d, x + 5 * d, y + 2 * d, fill=color2)
        canvas.create_rectangle(x, y + 2 * d, x + d, y + 3 * d, fill=color)
        canvas.create_rectangle(x, y + 3 * d, x + d, y + 4 * d, fill=color2)
        canvas.create_rectangle(x + d, y + 4 * d, x + 2 * d, y + 5 * d, fill=color)
        canvas.create_rectangle(x + 2 * d, y + 4 * d, x + 3 * d, y + 5 * d, fill=color2)
        canvas.create_rectangle(x + 3 * d, y + 4 * d, x + 4 * d, y + 5 * d, fill=color)
        canvas.create_rectangle(x + 4 * d, y + 5 * d, x + 5 * d, y + 6 * d, fill=color2)
        canvas.create_rectangle(x + 4 * d, y + 6 * d, x + 5 * d, y + 7 * d, fill=color)
        canvas.create_rectangle(x + 3 * d, y + 7 * d, x + 4 * d, y + 8 * d, fill=color2)
        canvas.create_rectangle(x + 2 * d, y + 7 * d, x + 3 * d, y + 8 * d, fill=color)
        canvas.create_rectangle(x + d, y + 7 * d, x + 2 * d, y + 8 * d, fill=color2)
        canvas.create_rectangle(x, y + 7 * d, x + d, y + 8 * d, fill=color)
        # A
        canvas.create_rectangle(x + 7 * d, y + d, x + 8 * d, y + 2 * d, fill=color2)
        canvas.create_rectangle(x + 8 * d, y + d, x + 9 * d, y + 2 * d, fill=color)
        canvas.create_rectangle(x + 9 * d, y + d, x + 10 * d, y + 2 * d, fill=color2)
        canvas.create_rectangle(x + 6 * d, y + 2 * d, x + 7 * d, y + 3 * d, fill=color)
        canvas.create_rectangle(x + 6 * d, y + 3 * d, x + 7 * d, y + 4 * d, fill=color2)
        canvas.create_rectangle(x + 6 * d, y + 4 * d, x + 7 * d, y + 5 * d, fill=color)
        canvas.create_rectangle(x + 6 * d, y + 5 * d, x + 7 * d, y + 6 * d, fill=color2)
        canvas.create_rectangle(x + 6 * d, y + 6 * d, x + 7 * d, y + 7 * d, fill=color)
        canvas.create_rectangle(x + 6 * d, y + 7 * d, x + 7 * d, y + 8 * d, fill=color2)
        canvas.create_rectangle(x + 7 * d, y + 4 * d, x + 8 * d, y + 5 * d, fill=color)
        canvas.create_rectangle(x + 8 * d, y + 4 * d, x + 9 * d, y + 5 * d, fill=color2)
        canvas.create_rectangle(x + 9 * d, y + 4 * d, x + 10 * d, y + 5 * d, fill=color)
        canvas.create_rectangle(x + 10 * d, y + 2 * d, x + 11 * d, y + 3 * d, fill=color2)
        canvas.create_rectangle(x + 10 * d, y + 3 * d, x + 11 * d, y + 4 * d, fill=color)
        canvas.create_rectangle(x + 10 * d, y + 4 * d, x + 11 * d, y + 5 * d, fill=color2)
        canvas.create_rectangle(x + 10 * d, y + 5 * d, x + 11 * d, y + 6 * d, fill=color)
        canvas.create_rectangle(x + 10 * d, y + 6 * d, x + 11 * d, y + 7 * d, fill=color2)
        canvas.create_rectangle(x + 10 * d, y + 7 * d, x + 11 * d, y + 8 * d, fill=color)
        # B
        canvas.create_rectangle(x + 12 * d, y + d, x + 13 * d, y + 2 * d, fill=color2)
        canvas.create_rectangle(x + 12 * d, y + 2 * d, x + 13 * d, y + 3 * d, fill=color)
        canvas.create_rectangle(x + 12 * d, y + 3 * d, x + 13 * d, y + 4 * d, fill=color2)
        canvas.create_rectangle(x + 12 * d, y + 4 * d, x + 13 * d, y + 5 * d, fill=color)
        canvas.create_rectangle(x + 12 * d, y + 5 * d, x + 13 * d, y + 6 * d, fill=color2)
        canvas.create_rectangle(x + 12 * d, y + 6 * d, x + 13 * d, y + 7 * d, fill=color)
        canvas.create_rectangle(x + 12 * d, y + 7 * d, x + 13 * d, y + 8 * d, fill=color2)
        canvas.create_rectangle(x + 12 * d, y + d, x + 13 * d, y + 2 * d, fill=color)
        canvas.create_rectangle(x + 12 * d, y + d, x + 13 * d, y + 2 * d, fill=color2)
        canvas.create_rectangle(x + 13 * d, y + d, x + 14 * d, y + 2 * d, fill=color)
        canvas.create_rectangle(x + 14 * d, y + d, x + 15 * d, y + 2 * d, fill=color2)
        canvas.create_rectangle(x + 15 * d, y + d, x + 16 * d, y + 2 * d, fill=color)
        canvas.create_rectangle(x + 16 * d, y + 2 * d, x + 17 * d, y + 3 * d, fill=color2)
        canvas.create_rectangle(x + 16 * d, y + 3 * d, x + 17 * d, y + 4 * d, fill=color)
        canvas.create_rectangle(x + 15 * d, y + 4 * d, x + 16 * d, y + 5 * d, fill=color2)
        canvas.create_rectangle(x + 14 * d, y + 4 * d, x + 15 * d, y + 5 * d, fill=color)
        canvas.create_rectangle(x + 13 * d, y + 4 * d, x + 14 * d, y + 5 * d, fill=color2)
        canvas.create_rectangle(x + 16 * d, y + 5 * d, x + 17 * d, y + 6 * d, fill=color)
        canvas.create_rectangle(x + 16 * d, y + 6 * d, x + 17 * d, y + 7 * d, fill=color2)
        canvas.create_rectangle(x + 15 * d, y + 7 * d, x + 16 * d, y + 8 * d, fill=color)
        canvas.create_rectangle(x + 14 * d, y + 7 * d, x + 15 * d, y + 8 * d, fill=color2)
        canvas.create_rectangle(x + 13 * d, y + 7 * d, x + 14 * d, y + 8 * d, fill=color)
        # I
        canvas.create_rectangle(x + 18 * d, y + d, x + 19 * d, y + 2 * d, fill=color2)
        canvas.create_rectangle(x + 19 * d, y + d, x + 20 * d, y + 2 * d, fill=color)
        canvas.create_rectangle(x + 20 * d, y + d, x + 21 * d, y + 2 * d, fill=color2)
        canvas.create_rectangle(x + 19 * d, y + 2 * d, x + 20 * d, y + 3 * d, fill=color)
        canvas.create_rectangle(x + 19 * d, y + 3 * d, x + 20 * d, y + 4 * d, fill=color2)
        canvas.create_rectangle(x + 19 * d, y + 4 * d, x + 20 * d, y + 5 * d, fill=color)
        canvas.create_rectangle(x + 19 * d, y + 5 * d, x + 20 * d, y + 6 * d, fill=color2)
        canvas.create_rectangle(x + 19 * d, y + 6 * d, x + 20 * d, y + 7 * d, fill=color)
        canvas.create_rectangle(x + 18 * d, y + 7 * d, x + 19 * d, y + 8 * d, fill=color2)
        canvas.create_rectangle(x + 19 * d, y + 7 * d, x + 20 * d, y + 8 * d, fill=color)
        canvas.create_rectangle(x + 20 * d, y + 7 * d, x + 21 * d, y + 8 * d, fill=color2)
        # N
        canvas.create_rectangle(x + 22 * d, y + d, x + 23 * d, y + 2 * d, fill=color)
        canvas.create_rectangle(x + 22 * d, y + 2 * d, x + 23 * d, y + 3 * d, fill=color2)
        canvas.create_rectangle(x + 22 * d, y + 3 * d, x + 23 * d, y + 4 * d, fill=color)
        canvas.create_rectangle(x + 22 * d, y + 4 * d, x + 23 * d, y + 5 * d, fill=color2)
        canvas.create_rectangle(x + 22 * d, y + 5 * d, x + 23 * d, y + 6 * d, fill=color)
        canvas.create_rectangle(x + 22 * d, y + 6 * d, x + 23 * d, y + 7 * d, fill=color2)
        canvas.create_rectangle(x + 22 * d, y + 7 * d, x + 23 * d, y + 8 * d, fill=color)
        canvas.create_rectangle(x + 23 * d, y + 3 * d, x + 24 * d, y + 4 * d, fill=color2)
        canvas.create_rectangle(x + 24 * d, y + 4 * d, x + 25 * d, y + 5 * d, fill=color)
        canvas.create_rectangle(x + 25 * d, y + 5 * d, x + 26 * d, y + 6 * d, fill=color2)
        canvas.create_rectangle(x + 26 * d, y + d, x + 27 * d, y + 2 * d, fill=color)
        canvas.create_rectangle(x + 26 * d, y + 2 * d, x + 27 * d, y + 3 * d, fill=color2)
        canvas.create_rectangle(x + 26 * d, y + 3 * d, x + 27 * d, y + 4 * d, fill=color)
        canvas.create_rectangle(x + 26 * d, y + 4 * d, x + 27 * d, y + 5 * d, fill=color2)
        canvas.create_rectangle(x + 26 * d, y + 5 * d, x + 27 * d, y + 6 * d, fill=color)
        canvas.create_rectangle(x + 26 * d, y + 6 * d, x + 27 * d, y + 7 * d, fill=color2)
        canvas.create_rectangle(x + 26 * d, y + 7 * d, x + 27 * d, y + 8 * d, fill=color)
        # A
        canvas.create_rectangle(x + 29 * d, y + d, x + 30 * d, y + 2 * d, fill=color2)
        canvas.create_rectangle(x + 30 * d, y + d, x + 31 * d, y + 2 * d, fill=color)
        canvas.create_rectangle(x + 31 * d, y + d, x + 32 * d, y + 2 * d, fill=color2)
        canvas.create_rectangle(x + 28 * d, y + 2 * d, x + 29 * d, y + 3 * d, fill=color)
        canvas.create_rectangle(x + 28 * d, y + 3 * d, x + 29 * d, y + 4 * d, fill=color2)
        canvas.create_rectangle(x + 28 * d, y + 4 * d, x + 29 * d, y + 5 * d, fill=color)
        canvas.create_rectangle(x + 28 * d, y + 5 * d, x + 29 * d, y + 6 * d, fill=color2)
        canvas.create_rectangle(x + 28 * d, y + 6 * d, x + 29 * d, y + 7 * d, fill=color)
        canvas.create_rectangle(x + 28 * d, y + 7 * d, x + 29 * d, y + 8 * d, fill=color2)
        canvas.create_rectangle(x + 29 * d, y + 4 * d, x + 30 * d, y + 5 * d, fill=color)
        canvas.create_rectangle(x + 30 * d, y + 4 * d, x + 31 * d, y + 5 * d, fill=color2)
        canvas.create_rectangle(x + 31 * d, y + 4 * d, x + 32 * d, y + 5 * d, fill=color)
        canvas.create_rectangle(x + 32 * d, y + 2 * d, x + 33 * d, y + 3 * d, fill=color2)
        canvas.create_rectangle(x + 32 * d, y + 3 * d, x + 33 * d, y + 4 * d, fill=color)
        canvas.create_rectangle(x + 32 * d, y + 4 * d, x + 33 * d, y + 5 * d, fill=color2)
        canvas.create_rectangle(x + 32 * d, y + 5 * d, x + 33 * d, y + 6 * d, fill=color)
        canvas.create_rectangle(x + 32 * d, y + 6 * d, x + 33 * d, y + 7 * d, fill=color2)
        canvas.create_rectangle(x + 32 * d, y + 7 * d, x + 33 * d, y + 8 * d, fill=color)
        x = x + 34 * d
    y = y + 8 * d
    x = x - 34 * times * d




canvas.mainloop()