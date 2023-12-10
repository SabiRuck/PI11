import tkinter

canvas = tkinter.Canvas()
canvas.pack()
x = 100
y = 50
lenght =  30

canvas.create_rectangle(x, y, x+lenght , y+lenght , fill="black")
canvas.create_rectangle(x+lenght , y, x+lenght*2, y+lenght , fill="black")
canvas.create_rectangle(x+lenght*2, y, x+lenght*3, y+lenght , fill="black" )
canvas.create_oval(x+lenght , y+lenght , x+lenght*2, y+lenght*2, fill="purple")
canvas.create_oval(x+lenght , y+lenght*2, x+lenght*2, y+lenght*3, fill="purple")
canvas.create_rectangle(x+lenght , y+lenght*3, x+lenght*2, y+lenght*4, fill="black")
canvas.create_rectangle(x, y+lenght*3, x+lenght , y+lenght*4, fill="black")
canvas.create_rectangle(x+lenght*2, y+lenght*3, x+lenght*3, y+lenght*4, fill="black")



canvas.mainloop()
