dosya = open("videogames.txt", "r")

lines = dosya.readlines()

selection = input("What game should I play? Choose between 1 and 10")

if selection =="1":
    print(lines[0], end="")
elif selection =="2":
    print(lines[1], end="")
elif selection =="3":
    print(lines[2], end="")
elif selection =="4":
    print(lines[1], end="")
elif selection =="5":
    print(lines[1], end="")
elif selection =="6":
    print(lines[1], end="")
elif selection =="7":
    print(lines[1], end="")
elif selection =="8":
    print(lines[1], end="")
elif selection =="9":
    print(lines[1], end="")
elif selection =="10":
    print(lines[1], end="")
else:
    print("That is not a number between 1 and 10.")

dosya.close()
