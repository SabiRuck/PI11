import tkinter, time, random

canvas = tkinter.Canvas(width=1000, heigh=300)
canvas.pack()
#canvas.delete(rectangle1)

""" #meni farbu
rectangle = canvas.create_rectangle(100, 100, 200, 200)
for i in range(5):
    canvas.update()
    time.sleep(1)
    color = random.choice(("red", "blue", "orange"))
    canvas.itemconfig(rectangle, fill=color)
"""

color1 = random.choice(("red", "blue", "pink", "orange"))
color2 = random.choice(("gray", "purple", "green", "yellow"))

o = 110
far1 = o
far2 = o
true = True

canvas.create_line(950, 0, 950, 300, width=3)
rectangle1 = canvas.create_rectangle(10, 10, o, 110, fill=color1)
rectangle2 = canvas.create_rectangle(10, 120, o, 220, fill=color2)

while true == True:
    x1 = random.randint(0, 5)
    x2 = random.randint(0, 5)
    canvas.update()
    time.sleep(0.001)
    canvas.move(rectangle1, x1, 0)  #rectangle1 je objekt, ktory sa bude posuvat, 100 = o kolko posunut na x a 0 = o kolko posunut na y
    canvas.move(rectangle2, x2, 0)
    far1 = far1 + x1
    far2 = far2 + x2
    if far1 >=950:
        print(f"{color1} rectangle win!")
        true = False

    if far2 >=950:
        print(f"{color2} rectangle win!")
        true = False



canvas.mainloop()

