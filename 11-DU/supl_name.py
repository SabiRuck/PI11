import tkinter as tk  #'as tk' = od teraz staci pisat tk a nie cele slovo tkinter

root = tk.Tk()  #vytvory tk okno
canvas = tk.Canvas(root, width = 600, height=400)  #velkost okna
canvas.pack()


#S
canvas.create_arc(25,50,75,100, start=10, extent=260, style="arc", outline="#7400b8", width=1)  #25=X-up left corner, 50=Y-up left corner, 75=X-down right corner, 100=Y-down right corner
canvas.create_arc(25,100,75,150, start=190, extent=260, style="arc", outline="#7400b8", width=1)
#A
canvas.create_line(100,150,125,50, fill="#8013BD", width=2)
canvas.create_line(125,50,150,150, fill="#8013BD", width=2)
canvas.create_line(108,120,142,120, fill="#8013BD", width=2)
#B
canvas.create_line(175,50,175,150, fill="#8B26C3", width=3)
canvas.create_arc(150,50,200,100, start=270, extent=180, style="arc", outline="#8B26C3", width=3)
canvas.create_arc(150,100,210,150, start=260, extent=190, style="arc", outline="#8B26C3", width=3)
#Í
canvas.create_line(230,50,230,150, fill="#9739C8", width=4)
canvas.create_line(230,40,240,25,fill="#9739C8", width=4)
#N
canvas.create_line(250,150,250,50, fill="#A24CCD", width=5)
canvas.create_line(250,50,300,150, fill="#A24CCD", width=5)
canvas.create_line(300,150,300,50, fill="#A24CCD", width=5)
#A
canvas.create_line(325,150,350,50, fill="#AE60D3", width=6)
canvas.create_line(350,50,375,150, fill="#AE60D3", width=6)
canvas.create_line(333,120,368,120, fill="#AE60D3", width=6)

#R
canvas.create_line(25,202,25,300, fill="#276221", width=7)
canvas.create_arc(0,200,75,250, start=250, extent=221, style="arc", outline="#276221", width=7)
canvas.create_line(27,250,75,300, fill="#276221", width=7)
#U
canvas.create_line(100,200,100,268, fill="#3b8132", width=8)
canvas.create_line(150,200,150,267, fill="#3b8132", width=8)
canvas.create_arc(99,233,150,300, start=180, extent=180, style="arc", outline="#3b8132", width=8)
#C
canvas.create_arc(175,200,225,300, start=45, extent=270, style="arc", outline="#46923c", width=9)
#K
canvas.create_line(250,200,250,300, fill="#52a447", width=10)
canvas.create_line(250,275,300,200, fill="#52a447", width=10)
canvas.create_line(260,260,300,300, fill="#52a447", width=10)
#O
canvas.create_oval(315,200,365,300, outline="#5bb450", width=11)
#V
canvas.create_line(375,200,400,300, fill="#72bf6a", width=12)
canvas.create_line(400,300,425,200, fill="#72bf6a", width=12)
#Á
canvas.create_line(435,300,460,200, fill="#8bca84", width=13)
canvas.create_line(460,200,485,300, fill="#8bca84", width=13)
canvas.create_line(445,260,475,260, fill="#8bca84", width=13)
canvas.create_line(460,195,472,180, fill="#8bca84", width=13)


root.mainloop()
