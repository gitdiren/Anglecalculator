try:
    num = int(input("What number should we divide 66 by?"))
    print( "Total = ", 66/num)       
except ValueError:
    print("You haven't entered a valid number")
except ZeroDivisionError:
    print("You can't divide by 0!What were you thinking?")
               
