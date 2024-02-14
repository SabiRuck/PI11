import turtle

t = turtle.Turtle()
t.speed(0)

def stvorec(width):
    for i in range(4):
        t.fd(width)
        t.left(90)

def sachovnica(d, color1, color2):
    x = -200
    y = 200
    for i in range(8):
        for j in range(8):
            t.pu()
            t.setpos(x, y)
            t.pd()
            t.fillcolor(color1)
            t.begin_fill()
            stvorec(d)
            t.end_fill()
            color1, color2 = color2, color1
            x += d
        x -= (d*8)
        y -= d
        color1, color2 = color2, color1



sachovnica(20, "purple", "black")

# for i in range(100):
#     stvorec(100)
#     t.left(360/100)

turtle.mainloop()