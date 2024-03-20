import tkinter

def flower(x, y, d, color):
    canvas.create_oval(x-d, y-d, x, y, fill=color)
    canvas.create_oval(x, y-d, x+d, y, fill=color)
    canvas.create_oval(x-d, y, x, y+d, fill=color)
    canvas.create_oval(x, y, x+d, y+d, fill=color)
    canvas.create_oval(x-d//2, y-d//2, x+d//2, y+d//2, fill="yellow")

def click(event):
    flower(event.x, event.y,times.get(), "red")

def button():
    global colorr
    m = 0
    colors = ["red", "blue", "green", "orange", "pink", "purple"]
    for color in colors:
        if m == 1:
            colorr = color
            break
        elif color == colorr:
            m = 1
    colorr = colors[0]

colorr = button()
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()
times = tkinter.Scale(orient="horizontal", from_=10, to=30, length=75)
times.pack()
tkinter.Button(text=colorr, command=button).pack()
canvas.bind("<ButtonPress>", click)


tkinter.mainloop()