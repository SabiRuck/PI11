f_mena = open("menaa.txt", "r", encoding="utf-8") #otrov subor na citanie ("r"), pisat ("w")
# f_mena = open("../mena.txt", "r") #hlada ho to o subor vyzsie (PI11)
# f_mena = open("C:/dokumenty/mena.txt", "r") #absolutna cesta k suboru

while True:
    riadok = f_mena.readline()
    if riadok == "":
        break
    print(riadok, end="")
    # print(riadok[:-1])# tu je bez \n


f_mena.close()






