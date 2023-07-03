def countdown(num):
    list = []

    for i in range(num, -1, -1):
        list.append(i)

    return list


print(countdown(5))


def print_and_return(list):
    print(list[0])

    return list[1]


print(print_and_return([1, 2]))


def first_plus_length(list):
    return list[0] + len(list)


print(first_plus_length([1, 2, 3, 4, 5]))


def values_greater_than_second(list):
    if len(list) < 2:
        return False

    second = list[1]
    count = 0
    new_list = []

    for num in list:
        if num > second:
            count += 1
            new_list.append(num)

    print(f'The count of numbers larger than second: {count}')

    return new_list


print(values_greater_than_second([5, 2, 3, 2, 1, 4]))


def length_and_value(length, value):
    list = []

    for i in range(length):
        list.append(value)

    return list


print(length_and_value(4, 7))
print(length_and_value(6, 2))
