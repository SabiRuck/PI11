spol, sam = 0, 0
sss = input("input: ")

for s in sss:
    if s in "aeiouyáéíóúýä":
        sam += 1
    else:
        spol += 1

print(f"spoluhlasok: {spol}\nsamohlasok: {sam}")