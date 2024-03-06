import turtle
turtle.speed(0)
turtle.delay(0)

t1 = turtle.Turtle()
t2 = turtle.Turtle()


t1.pu()
t2.pu()
t1.setpos(100, 0)
t2.setpos(-100, 0)
t1.pd()
t2.pd()

def idk(flowers, times, wight):
    for i in range(times):
        for j in range(4):
            t1.fd(wight)
            t2.fd(wight)
            t1.lt(90)
            t2.lt(90)
        t1.lt(360//times)
        t2.lt(360//times)

idk(10, 50)

turtle.mainloop()