# 1
def number_of_food_groups():
    return 5


# print(number_of_food_groups()) # prints 5


# 2
def number_of_military_branches():
    return 5


# print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3) + # name error
#       number_of_military_branches())


# 3
def number_of_books_on_hold():
    return 5
    return 10  # statement won't be run because the first return statement exited the function


# print(number_of_books_on_hold())


# 4
def number_of_fingers():
    return 5
    print(10)  # print statement won't be run for the same reason as stated above


# print(number_of_fingers())


# 5
def number_of_great_lakes():
    print(5)


# x = number_of_great_lakes() # prints 5
# print(x) # prints none because nothing was returned


# 6
def add(b, c):
    print(b+c)


# print(add(1, 2) + add(2, 3)) # prints 3 and 5 and then gives a type error because you can't add things when nothing was returned


# 7
def concatenate(b, c):
    return str(b)+str(c)


# print(concatenate(2, 5)) # prints 25


# 8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)  # print 100
    if b < 10:  # doesn't get run
        return 5
    else:
        return 10  # returns 10
    return 7  # never runs because the if / else can't be passed


# print(number_of_oceans_or_fingers_or_continents())  # prints 100 and then 10


# 9
def number_of_days_in_a_week_silicon_or_triangle_sides(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3  # never runs because of if / else is impassable


# print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3)) # prints 7
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5, 3)) # prints 14
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3) + # prints 21
#       number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))


# 10
def addition(b, c):
    return b+c
    return 10  # doesn't run because of the first return statement


# print(addition(3, 5)) # prints 8


# 11
b = 500
# print(b)  # prints 500


def foobar():
    b = 300
    print(b)


# print(b)  # prints 500
# foobar()  # prints 300
# print(b)  # prints 500


# 12
b = 500
# print(b)  # prints 500


def foobar():
    b = 300
    print(b)
    return b


# print(b) # prints 500
# foobar() # prints 300, returns 300 but doesn't print anything from the return statement
# print(b)


# 13
b = 500
# print(b)


def foobar():
    b = 300
    print(b)
    return b


# print(b) # prints 500
# b = foobar() # prints 300 and sets b to 300
# print(b) # prints 300


# 14
def foo():
    print(1)
    bar()
    print(2)


def bar():
    print(3)


# foo()  # prints 1, 3, 2


# 15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10


def bar():
    print(3)
    return 5


# y = foo()  # prints 1, 3, 5, sets y to 10
# print(y)  # prints 10
