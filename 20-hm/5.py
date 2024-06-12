import tkinter as Tk, random as ran

canvas = Tk.Canvas(height=500, width=500)
canvas.pack()
def generate(m=500, n=4):
    c = ""
    for i in range(n):
        c += f"{ran.randint(0, m)} "
    return c[:-1]


with open("idk.txt", "w") as file:
    for _ in range(10):
        file.write(f"{ran.choice(('r', 'o'))} {generate()}\n")
        file.write(f"{generate(255)}\n")


with open("idk.txt", "r") as file:
    first = file.readline()[:-1]
    while first != '':
        second = file.readline()[:-1]

        coords = first[2:].split(" ")
        rgb = [int(e) for e in second.split(" ")]
        color = f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'

        if first[0] == "r":
            canvas.create_rectangle(*coords, fill=color)
        elif first[0] == "o":
            canvas.create_oval(*coords, fill=color)

        first = file.readline()[:-1]

















canvas.mainloop()