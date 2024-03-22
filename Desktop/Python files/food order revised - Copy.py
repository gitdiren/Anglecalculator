print("Welcome to Pete Porker's Pork Pie Emporium")

total = 0
while True:
  noOfEggs = int(input("Scotch eggs are 49p each. Enter your amount to order:"))
  if noOfEggs >= 0 :
   print("you selected", noOfEggs, "scotch eggs")
   
  noOfPorkPies = int(input("Pork pies are 85p each. Enter your amount to order:"))
  if noOfPorkPies >= 0:
   print("you selected", noOfPorkPies, "pork pies") 
  
  noOfQuicheTarts = int(input("Quiche tarts are £1.45 each.Enter your amount to order:"))
  if noOfQuicheTarts >= 0:
    print("you selected", noOfQuicheTarts, "quiche tarts") 
    break

while True:
  choice = input ("Are you happy with this selection?")
  if choice == "yes" :
   print("Receipt for Pete Porker's Pork Pie Emporum")
   totalEggs= noOfEggs * 0.49
   print (noOfEggs, "scotch eggs = £", totalEggs)
   totalPorkPies = noOfPorkPies * 0.85
   print (noOfPorkPies, "pork pies = £", totalPorkPies )
   totalQuicheTarts = noOfQuicheTarts * 1.45
   print ( noOfQuicheTarts, "quiche tarts = £", totalQuicheTarts)
   sum = round (totalEggs + totalPorkPies + totalQuicheTarts)
   print("Total = £ ", sum )
   break

  elif choice == "no":
     print("Pls try again")


 

