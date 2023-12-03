import tkinter
import random

canvas = tkinter.Canvas(width=500, height=400)
canvas.pack()

""" 
name = "Jan"
name2 = "Mrkvicka"
age = 255

print(f"Volam sa {name} {name2} a mam {age:02x}.")    #{age;03} = 012  #{age:02x} = 02=pocet cifier a x prevedie do 16-kovej sustavy
"""
rn =random.randint(10, 40)

for i in range(rn):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color= f"#{r:02x}{g:02x}{b:02x}"

    x = random.randint(2, 482)
    y = random.randint(2, 482)
    d = 60
    d2 = d//2

    canvas.create_oval(x-d2, y-d2, x+d2, y+d2, fill=color)





canvas.mainloop()
