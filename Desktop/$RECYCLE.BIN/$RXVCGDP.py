def readAndSearch():
    file = open("poem.txt", "r")
   
    while True:
        searchFor = "Its fleece was white as snow"
        line = file.readline()
        if line == searchFor:
            print("Its fleece was white as snow")
            break


readAndSearch()
