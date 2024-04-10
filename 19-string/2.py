ret = input("zadaj retazec: ")
pos = int(input("posun: "))
# for i in range(len(retazec)):
#     print(i, retazec[i])
#
# i = 0
# for znak in retazec:
#     print(i, znak)
#     i += 1

# for i, znak in enumerate(retazec):
#      print(i, znak)

# for i, znak in enumerate(retazec):
#     print(i+1, znak)
# print()
# for i, znak in enumerate(retazec[::-1]):
#     print(-1-i, znak)

for i in ret:
    print(f'{i}- {ord(i)}')
kod = ""
for i in ret:
    kod += chr(ord(i)+pos)

print(kod)