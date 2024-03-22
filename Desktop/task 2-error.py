
try:
    num = int(input("Enter a number to be divided by 999:"))
    print(999/num)  
except ValueError:
    print("You haven't entered a valid no!")
except ZeroDivisionError:
    print("you can't divide by 0!")
