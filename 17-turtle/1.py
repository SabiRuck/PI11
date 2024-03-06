import turtle
t = turtle.Turtle()
turtle.delay(0)

def main():
    for i in range(3, 17):
        n_uholnik(i, 50)


def square(width):
        for _ in range(4):
            t.fd(width)
            t.rt(90)

def n_uholnik(n, width):
    for _ in range(n):
        t.fd(width)
        t.lt(360/n)




if __name__ == "__main__":
    main()
turtle.mainloop()