import random

def rgb(r = 255, g = 255, b = 255):
    r = random.randint(0, r)
    g = random.randint(0, g)
    b = random.randint(0, b)



    return f"#{r:02x}{g:02x}{b:02x}"