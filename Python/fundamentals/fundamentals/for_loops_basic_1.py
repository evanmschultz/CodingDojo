def print_ints(max):
    for i in range(max + 1):
        print(i)


# print_ints(150)

def multiples_of_5(max):
    for i in range(5, max + 1, 5):  # from 5 to max in steps of 5, no modulo needed
        print(i)


# multiples_of_5(1000)


def dojo_count(max):
    for i in range(1, max + 1):
        if i % 5 == 0:
            if i % 10 == 0:
                print('Coding Dojo')
            else:
                print('Coding')
        else:
            print(i)


# dojo_count(100)


def add_odds(max):
    sum = 0

    for i in range(1, max + 1, 2):
        sum += i

    return sum


# print(add_odds(500000))


def count_down_by_fours(max):
    count = max

    while count > 0:
        print(count)

        count -= 4


# count_down_by_fours(2018)


def flexible_counter(low, high, multiple, direction='up'):
    increment = multiple

    if direction == 'down':
        increment *= -1
        low, high = high, low - 1
    else:
        high += 1

    for i in range(low, high, increment):  # faster to not use modulus operator
        print(i)


# flexible_counter(1, 100, 3, 'down')
low = int(input('Enter the low number to count from or to: '))
high = int(input('Enter the high number to count to or from: '))
multiple = int(input('Enter the multiple to count by: '))
direction = input(
    'Enter up or down to indicate the direction you want to count, if left blank it will be set to up: ')

flexible_counter(low, high, multiple, direction)
