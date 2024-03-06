import turtle, random, random_color
t = turtle.Turtle()
turtle.delay(0)
t.speed(0)

def obluk(d):
    for _ in range(9):
        t.fd(d)
        t.lt(10)

def lupen(d):
    for _ in range(2):
        obluk(d)
        t.lt(90)

def kvet(pocet, d):
    r = 255
    for i in range(pocet):
        t.fillcolor(f"#{r:02x}{0:02x}{0:02x}")
        t.begin_fill()
        lupen(d)
        t.right(360/pocet)
        t.end_fill()
        r -= 255//pocet


def move(mutch):
    t.pu()
    t.fd(mutch)
    t.pd()

def kvety(pocet, d, krat = 1):
    kvet(pocet, d)
    move(9*pocet *2)
    kvet(pocet, d)

def main():






if __name__ == "__main__":
    main()
turtle.mainloop()