import  tkinter

canvas = tkinter.Canvas()
canvas.pack()

x = 5
y = 5
d = 10
color = "pink"

canvas.create_rectangle(x, y, x+d, y+d, fill = color)
canvas.create_rectangle(x+d, y+d, x+2*d, y+2*d, fill = color)
canvas.create_rectangle( x+2*d, y+2*d, x+3*d, x+3*d, fill = color)
canvas.create_rectangle( x+3*d, y+3*d, x+4*d, x+4*d, fill = color)
canvas.create_rectangle( x+4*d, y+4*d, x+5*d, x+5*d, fill = color)
canvas.create_rectangle(x, y+4*d, x+d, x+5*d, fill = color)
canvas.create_rectangle( x+d, y+3*d, x+2*d, y+4*d, fill = color)
canvas.create_rectangle( x+3*d, y+d, x+4*d, y+2*d, fill = color)
canvas.create_rectangle(x+4*d, y, x+5*d, y+d, fill = color)

x = d*6
y = 5
color = "red"

canvas.create_rectangle(x, y, x+d, y+d, fill = color)
canvas.create_rectangle(x+d, y+d, x+2*d, y+2*d, fill = color)
canvas.create_rectangle( x+2*d, y+2*d, x+3*d, x+3*d, fill = color)
canvas.create_rectangle( x+3*d, y+3*d, x+4*d, x+4*d, fill = color)
canvas.create_rectangle( x+4*d, y+4*d, x+5*d, x+5*d, fill = color)
canvas.create_rectangle(x, y+4*d, x+d, x+5*d, fill = color)
canvas.create_rectangle( x+d, y+3*d, x+2*d, y+4*d, fill = color)
canvas.create_rectangle( x+3*d, y+d, x+4*d, y+2*d, fill = color)
canvas.create_rectangle(x+4*d, y, x+5*d, y+d, fill = color)







canvas.mainloop()