file = open("classlist.txt", "r")

search_name = input("Which student are you searching for?")

found = "false"

for line in file:
    if search_name in line:
        print(line, end="")
        found = "true"
if found == "false":
    print("Student not found")

file.close()
