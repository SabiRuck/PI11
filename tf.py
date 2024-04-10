import tkinter, random, time

window = tkinter.Tk()

height, width = 600, 300
canvas = tkinter.Canvas(height=height, width=width, background="#202020")
canvas.pack()
speed = 10

class Car:
    def __init__(self):
        class Idk():
            def __init__(self):
                while True:
                    try:  # create car
                        self.part1 = canvas.create_rectangle(self.x - 15, self.y, self.x + 15, self.y + 50, fill="red")
                        self.part2 = canvas.create_rectangle(self.x - 10, self.y + 13, self.x + 10, self.y + 23,
                                                             fill="blue")
                        self.part3 = canvas.create_rectangle(self.x - 20, self.y + 10, self.x - 15, self.y + 20,
                                                             fill="black")
                        self.part4 = canvas.create_rectangle(self.x + 15, self.y + 10, self.x + 20, self.y + 20,
                                                             fill="black")
                        self.part5 = canvas.create_rectangle(self.x - 20, self.y + 30, self.x - 15, self.y + 40,
                                                             fill="black")
                        self.part6 = canvas.create_rectangle(self.x + 15, self.y + 30, self.x + 20, self.y + 40,
                                                             fill="black")
                        break
                    except AttributeError:  # create first x, y
                        self.x = width // 2
                        self.y = height - 150

            def move(self, x2):  # change x, delete car, create car
                self.x = x2
                canvas.delete(self.part1)
                canvas.delete(self.part2)
                canvas.delete(self.part3)
                canvas.delete(self.part4)
                canvas.delete(self.part5)
                canvas.delete(self.part6)
                self.__init__()

            @property
            def return_x(self):
                return self.x

        self.car = Idk()

    def move_right(self, z):  # moves to right by z
        self.car.move(self.car.return_x + z)

    def move_left(self, z):  # moves to left by z
        self.car.move(self.car.return_x - z)

    @property
    def coords(self):
        return [self.car.return_x - 20, height - 150, self.car.return_x + 20, height - 100]


class Road:
    def __init__(self):
        while True:
            try:
                for _ in range(int((height//50.0)+1)):
                    line = canvas.create_line(width//2, self.h, width//2, self.h+30, fill="#C0C0C0", width=5)
                    self.lines.insert(0, line)
                    self.h += 50
                break
            except AttributeError:
                self.h = -30
                self.lines = []

    def move(self):
        global speed
        canvas.update()
        canvas.after(1)
        for line in self.lines:
            canvas.move(line, 0, speed)

            if canvas.coords(line)[1] > height:
                self.lines.remove(line)
                canvas.delete(line)

            elif canvas.coords(line)[3] == 50:
                new_line = canvas.create_line(width//2, -30, width//2, 0, fill="#C0C0C0", width=5)
                self.lines.append(new_line)


class Rocks:
    def __init__(self):
        self.rocks = []  # all future rocks
        self.points = 0
        self.point = 1
        self.size = random.randint(25, 40)  # rock size

        x = random.randint(0, width - self.size)  # first x
        canvas.update()
        canvas.after(500)

        self.rock = canvas.create_rectangle(x, 0, x + self.size, self.size,
                                            fill=random.choice(("#003319", "#281515", "#404040")))  # first rock
        self.rocks.append(self.rock)  # first rock is added to list

    def add_rock(self):  # add otrer rocks
        x = random.randint(0, width - self.size)  # choose x for new rock
        self.size = random.randint(20, 30)
        last = canvas.coords(self.rocks[len(self.rocks) - 1])  # coords of last sreated rock

        if (last[1] > 60 + self.size or (
                (x > last[2] + 40 or x < last[0] - 40 - self.size) and last[1] > 50)) and random.randint(1, 5) == 1:
            # y distance from last, x distance from right of last, x distance from left of last, some distance from last
            # must be greater that size car size, from right greater that car width, from left greater than car width

            self.rock = canvas.create_rectangle(x, 0, x + self.size, self.size,
                                                fill=random.choice(("#003319", "#281515", "#404040")))
            self.rocks.append(self.rock)

    def move_rocks(self, coords):
        global speed
        for rock in self.rocks:  # each rock moves
            canvas.update()
            canvas.after(1)
            canvas.move(rock, 0, speed)
            rcoords = canvas.coords(rock)

            if rcoords[1] > height:  # if rock no longer in canva == delete
                canvas.delete(rock)
                self.rocks.remove(rock)
                self.points += self.point

                # if self.points in range(15, 3000, 15):
                #     speed += 5

            elif ((rcoords[0] in range(coords[0], coords[2])) or (rcoords[2] in range(coords[0], coords[2]))) and (
            (rcoords[1] in range(coords[1], coords[3]) or (rcoords[3]) in range(coords[1], coords[3]))):
                raise DeathError

    @property
    def score(self):
        return self.points


class DeathError(Exception):
    "You died!"
    pass


def main():
    button.destroy()
    a = 0
    road = Road()
    car = Car()
    canvas.after(500)
    rocks = Rocks()

    while True:
        try:
            def right(event):
                if a == 0:
                    car.move_right(13)
            def left(event):
                if a == 0:
                    car.move_left(13)

            canvas.bind_all("<Right>", right)
            canvas.bind_all("<Left>", left)

            road.move()
            rocks.move_rocks(car.coords)
            rocks.add_rock()

            if car.coords[2] <= 2 or car.coords[0] >= width:
                raise DeathError

        except DeathError:
            canvas.delete("all")
            canvas.create_text(width // 2, height // 2, text=f"You died!\nYou'r score is {rocks.score}",font='arial 30')
            a = 1
            break


button = tkinter.Button(window, text='PLAY', command=main)
button.pack()

canvas.mainloop()