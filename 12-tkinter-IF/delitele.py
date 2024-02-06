# while True:
#     try:
#         num = int(input("Enter number: "))
#
#         if num == 0:
#             print("It's 0. Bye!")
#             break
#         elif num % 2 == 0:
#             print("Parne.")
#         else:
#             print("Neparne.")
#
#     except ValueError:
#         print("Enter a number.")

while True:
    try:
        divisors = []
        num = int(input("Enter number: "))
        print("Divisors: ", end="")
        x = 0
        for i in range(1, num + 1):
            if num == 0:
                break
            elif (num % i) == 0:
                x += 1
                print(i, end="")

                '''
                divisors.append(i)
        print(f"Divisors are{divisors}")
        '''
        print()
        print(f"Number of divisors: {x}")
        if x == 2 or x == 1:
            print("Number is prime number.")

    except ValueError:
        print("Enter a number.")