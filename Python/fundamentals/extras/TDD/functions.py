def reverse_list(list: list) -> list:
    '''
        Function to reverse a list in place.

        Example:
            reverse_list([1, 2, 3]) output: [3, 2, 1]
    '''

    left, right = 0, len(list) - 1
    while left < right:
        # swap values at left and right pointers
        list[left], list[right] = list[right], list[left]

        # move pointers
        left, right = left + 1, right - 1

    # print(list)
    return list


def is_palindrome(string: str) -> bool:
    '''
        Function to check if a string is a palindrome, ignoring special characters.

        Example:
            is_palindrome('Race car') output: True
    '''

    left, right = 0, len(string) - 1

    # iterate until left and right meet
    while left < right:
        # while still checking inside the string, check if string[left] is alphanumeric
        while left < right and not string[left].isalnum():
            # if not alpha numeric, pass it
            left += 1
        # same for the right
        while left < right and not string[right].isalnum():
            right -= 1

        # check if the left and right characters are equal regardless of case
        if string[left].lower() != string[right].lower():
            return False

        # move pointers
        left, right = left + 1, right - 1

    # if all characters were equal, return True
    return True


def coins(num):
    '''
        Function to tell you what coins to give as change in quarters, dimes, nickels, and 
        pennies, minimizing the number of coins.

        Example:
            coins(23) output: [0, 2, 0, 3] # two dimes and three quarters
    '''
    # ignore anything that can be given back as a bill
    num %= 100

    # values of each coin type
    denominations = [25, 10, 5, 1]
    # amount of each coin type to given as change
    counts = []

    for value in denominations:
        # find count of each type of coin
        count = num // value
        # add to counts list
        counts.append(count)
        # update num by subtracting the value given in the coin
        num -= count * value

    return counts


def factorial(num):
    '''
        Function that returns the factorial of num using recursion.

        Example:
            factorial(5) output: 120
    '''

    if num < 0:
        return None
    # base case, prevents further recursion
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def fibonacci(n):
    '''
        Function that returns the nth value of fibonacci recursion.

        Example:
            fibonacci(5) output: 5
    '''
    if n < 0:
        return None
    # base case is 0 or 1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    # a fibonacci number is the sum of the two previous numbers
    else:
        # recursively call the function to find (n - 1) and (n - 2) at the base case(s) and then build back up to n
        return fibonacci(n - 1) + fibonacci(n - 2)
