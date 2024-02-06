import tkinter

canvas = tkinter.Canvas(width=600)
canvas.pack()

def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def stvorec(x, y, times, d, r=0, g=0, b=0):
    for i in range(times):
        krok = 255 // (times + 1)
        canvas.create_rectangle(x, y, x + d, y + d, fill=rgb(r,g,b))
        if r >= krok:
            r -= krok
        if g >= krok:
            g -= krok
        if b >= krok:
            b -= krok
        x += d

def main():
    stvorec(10, 10, 20, 20, 255)
    stvorec(10, 40, 20, 20, 0, 255)
    stvorec(10, 70, 20, 20, 0, 0, 255)




main()
canvas.mainloop()