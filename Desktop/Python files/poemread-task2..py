def readOneLineATime():
    file = open("poem.txt", "r")
    while file:
        line = file.readline()
        print(line)
        if line == "":
          break
readOneLineATime()
