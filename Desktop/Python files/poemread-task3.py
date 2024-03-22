def readAndSearch():
    file = open("poem.txt", "r")
    searchFor = "Its fleece was white as snow"
    for line in file:
        if searchFor in line:
            print(searchFor)
            
  

readAndSearch()

