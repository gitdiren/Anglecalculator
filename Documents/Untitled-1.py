
'''Task 1
Write a Python program that utilizes different data types like integers, floats, strings, lists,
tuples, and dictionaries. Include examples of arithmetic, comparison and logical
operators.
Task 2
Write a Python program that implements the following:
1. User input and print statements
2. Conditional statements (if, elif, else)
3. Loops (for, while)
4. Built-in functions like len(), range(), input()'''


#Task 1 & Task 2
#using dictionaries and tuples

my_dictionary = {
    "name": "Ayse",
    "age": 24,
    "weight": 79 
    }
my_dictionary['weight'] = 67.8
print(my_dictionary)

#changing dictionary value
my_dictionary['weight'] = int(67.8)
print(my_dictionary)


my_tuple = ('summer','winter','autumn','spring')
print(type(my_tuple))

# using built in functions like len() and type(), looping through lists

fruits = ['banana', 'apple','orange','melon','strawberry','raspberry']

for fruit in fruits:
    print(f'my favourite fruit is {fruit}')

print(len(fruits))
print(type(fruits))

#using arithmetic operators
print('The addition of the no of items in my tuple and fruits is: ', len(fruits)+len(my_tuple))
print('The subtraction of the no of items in my tuple and fruits is: ', len(fruits) - len(my_tuple))
print('The division of the no of items in my tuple and fruits is: ', len(fruits) / len(my_tuple))
print('The multiplication of the no of items in my tuple and fruits is: ', len(fruits) * len(my_tuple))

#using range()

for number in range(0,5):
    print(number)

#guesing the number: this is a game where the user is trying to find out the number that was pre-set.

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
    

