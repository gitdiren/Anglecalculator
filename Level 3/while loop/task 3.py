total = 0
while True:
  number = int(input("Enter a number:  "))
  total = number + total
  print("The total is ", total)
  
  if total >= 100:
    print ("Program finished")
    break
