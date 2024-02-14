import turtle,

t = turtle.Turtle()
t.speed(0)

def stvorec(width):
    for i in range(4):
        t.fd(width)
        t.left(90)

# for i in range(4):
#     for j in range(1, 11):
#         stvorec(10*j)
#     t.left(90)

def stvorce(times):
    x = 23
    for i in range(1, times+1):
        stvorec(x)
        t.pu()
        t.right(135)
        t.fd(20)
        t.pd()
        t.left(135)
        x+= 30

stvorce(10)
turtle.mainloop()