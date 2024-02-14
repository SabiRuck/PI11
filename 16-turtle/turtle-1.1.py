import turtle, random as r

t = turtle.Turtle()
t.speed(-10)
def stvorec(width):
    for i in range(4):
        t.fd(width)
        t.left(90)

for i in range(100):

    t.pu()
    t.setpos(r.randint(-200, 200), r.randint(-200, 200))
    t.seth(r.randint(0, 359))
    t.pd()
    t.fillcolor(r.choice(("red", "blue", "green", "orange", "yellow")))
    t.begin_fill()
    stvorec(30)
    t.end_fill()

turtle.mainloop()