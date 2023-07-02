num1 = 42  # int, variable declaration
num2 = 2.3  # float, variable declaration
boolean = True  # boolean, variable declaration
string = 'Hello World'  # string, variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalapenos',  # list, initialize
                  'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake',  # dictionary, initialize
          'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')  # tuple, initialize
print(type(fruit))  # log, type check
print(pizza_toppings[1])  # log, access value of list
pizza_toppings.append('Mushrooms')  # add value to list
print(person['name'])  # log, access value of dictionary
person['name'] = 'George'  # change value of dictionary
person['eye_color'] = 'blue'  # add key, value pair to dictionary
print(fruit[2])  # log, access value of tuple

if num1 > 45:  # conditional, if statement
    print("It's greater")  # log, print string
else:  # conditional, else statement
    print("It's lower")  # log, string

if len(string) < 5:  # conditional, if, length check on string
    print("It's a short word!")
elif len(string) > 15:  # else if conditional
    print("It's a long word!")
else:  # else conditional
    print("Just right!")

for x in range(5):  # for loop, output: 0, 1, 2, 3, 4
    print(x)
for x in range(2, 5):  # for loop, output: 2, 3, 4
    print(x)
for x in range(2, 10, 3):  # for loop, output: 2, 5, 8
    print(x)
x = 0  # reassign variable
while (x < 5):  # while loop
    print(x)  # output: 0, 1, 2, 3, 4
    x += 1  # update variable, this while loop acts like a for loop

pizza_toppings.pop()  # delete last value in list, returns 'olives'
pizza_toppings.pop(1)  # delete second item in list, returns '

# log person dictionary, output: {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': 'blue'}
print(person)
# deletes 'eye_color' key, value from person dictionary pair returns key, value
person.pop('eye_color')
# log person dictionary, output: {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
print(person)

for topping in pizza_toppings:  # for loop value in pizza_toppings list
    if topping == 'Pepperoni':  # conditional if statement
        continue  # moves to next item in list if current item equals 'Pepperoni'
    # logs string each time the loop runs minus the time 'Pepperoni' is the current value
    print('After 1st if statement')
    if topping == 'Olives':  # conditional if statement
        break  # if current value is 'Olives' the program exits loop


def print_hello_ten_times():  # function declaration without a parameter
    for num in range(10):  # for loop num goes from 0-9
        print('Hello')  # logs string 'Hello' ten times


print_hello_ten_times()  # function call


def print_hello_x_times(x):  # function declaration with parameter
    for num in range(x):  # for loop from 0 to (x - 1)
        print('Hello')  # prints 'Hello' x times


print_hello_x_times(4)  # function call with 4 as the parameter


# function declaration with parameter x set to 10 as default
def print_hello_x_or_ten_times(x=10):
    for num in range(x):  # for loop from 0 to (x - 1), 0 to 9 if no parameter is passed in
        print('Hello')  # prints 'Hello' x times


print_hello_x_or_ten_times()  # function call with no parameter, uses default: x=10
print_hello_x_or_ten_times(4)  # function call with 4 as parameter


"""
Bonus section
"""

# print(num3) # NameError: name <variable name> is not defined
# num3 = 72 # define num3 variable
# fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team' / because the key does not exist
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) # IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'
