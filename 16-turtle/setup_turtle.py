import turtle

t = turtle.Turtle()
def main():
    turtle.speed(-10)
    stvorec(10)
    turtle.mainloop()

def stvorec(width):
    for i in range(4):
        t.fd(width)
        t.left(90)




if __name__ == "__main__":
    main()