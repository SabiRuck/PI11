import turtle
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
    for i in range(pocet):
        lupen(d)
        t.right(360/pocet)

def main():
    kvet(10, 20)


if __name__ == "__main__":
    main()
turtle.mainloop()