'''Task 1&2
Write a Python program that utilizes different data types like integers, floats, strings, lists,
tuples, and dictionaries. Include examples of arithmetic, comparison and logical
operators.
Task 2
Write a Python program that implements the following:
1. User input and print statements
2. Conditional statements (if, elif, else)
3. Loops (for, while)
4. Built-in functions like len(), range(), input()'''



#Task 1
#using dictionaries

my_dictionary = {
    "name": "Ayse",
    "age": 24,
    "weight": 79 
    }
my_dictionary['weight'] = 67.8
print(my_dictionary)

my_dictionary['weight'] = int(67.8)
print(my_dictionary)

# using built in functions like len() and type(), 

fruits = ['banana', 'apple','orange','melon']


print(len(fruits))
print(type(fruits))

#looping through lists

for fruit in fruits:
    print(f'my favourite fruit is {fruit}')



#Task 2: guesing the number: this is a game where the user is trying to find out the number that was pre-set.

print('Guess My Number')

while True:
    picked_no = 6
    number = int(input('pick a number from 0 to 10: '))
    if number > picked_no:
        print('You picked a number bigger than my number!')
        continue
    elif number < picked_no:
        print('You picked a number smaller than my number!')
        continue
    else:
        print('Well done! you found my number!')
        break
    
