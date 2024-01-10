while True:
    n = int(input("Enter number: "))

    for num in range(1, n +1):
        x = 0
        if num == 0:
            break
        for i in range(1, num + 1):
            if (num % i) == 0:
                x += 1
        if x == 2:
            print(num, end=" ")
    print()



