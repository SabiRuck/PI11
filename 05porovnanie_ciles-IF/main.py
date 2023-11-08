
a = int(input("first number: ",))
b = int(input("second number: "))
c = int(input("third number: "))
d = int(input("fourth number: "))
e = int(input("fifth number: "))

#biggest = " "

"""
if a == b == c:
    print("They are same.")
else:
    if a > b:
        if a > c:
            biggest = a
        else:
            biggest = c
        print("Biggest number is: ", biggest)
    else:
        if b > c:
            biggest = b
        else:
            biggest = c
        print("Biggest number is: ", biggest)
"""
max = a

if a == b == c == d == e:
    print("They are same.")
else:
    if max < b:
        max = b
    if max < c:
        max = c
    if max < d:
        max = d
    if max < e:
        max = e

    print(max, "is biggest.")



