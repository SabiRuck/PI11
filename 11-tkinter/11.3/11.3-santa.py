import tkinter, time, random

width = 600
height = 600
santa_x = width // 2
santa_y = 66
santa2_x = (width // 4)*3
santa2_y = 66
santa3_x = (width // 4)
santa3_y = height - 64
santa2_move = 2
santa_move = 2
santa3_move = 2

print(santa2_x)

canvas = tkinter.Canvas(height=height, width=width)
canvas.pack()

image_santa = tkinter.PhotoImage(file="santa.png")
santa = canvas.create_image(santa_x, santa_y, image=image_santa)
santa2 = canvas.create_image(santa2_x, santa2_y, image=image_santa)
santa3 = canvas.create_image(santa3_x, santa3_y, image=image_santa)

while True:
    canvas.update()
    time.sleep(0.01)

    canvas.move(santa, 0, santa_move)
    santa_y = santa_y + santa_move

    canvas.move(santa2, 0, santa2_move)
    santa2_y = santa2_y + santa2_move

    canvas.move(santa3, 0, - santa3_move)
    santa3_y = santa3_y - santa_move

    if santa3_y <= -64:
        canvas.delete(santa3)
        santa3_y = height - 64
        santa3 = canvas.create_image(santa3_x, santa3_y, image=image_santa)


    if santa2_y == height -64:
        santa2_move = - santa2_move
    if santa2_y <= 64:
        santa2_move = - santa2_move

    if santa_y == height + 64:
        canvas.delete(santa)
        santa_y = 66
        santa = canvas.create_image(santa_x, santa_y, image=image_santa)








canvas.mainloop()