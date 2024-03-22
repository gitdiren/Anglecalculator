file = open("mates.txt", "r")
for line in file:
    if "Cassie" in line:
        print("ok! you found it!")
file.close()

#or we would write first line.. with open("mates.txt", "r") as file:
