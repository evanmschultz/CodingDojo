x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)

'''
    done - 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
    done - 2. Change the last_name of the first student from 'Jordan' to 'Bryant'
    done - 3. In the sports_directory, change 'Messi' to 'Andres'
    done - 4. Change the value 20 in z to 30
'''


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


'''
    Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops 
    through each dictionary in the list and prints each key and the associated value. For example, given 
    the following list:
'''


def iterateDictionary(list):
    for dict in list:
        output_string = ''

        for key, value in dict.items():
            output_string += f'{key} - {value}'

            if key == 'first_name':
                output_string += ', '

        print(output_string)


def iterateDictionaryListComprehension(list):
    for dict in list:
        output_string = ', '.join(
            f'{key} - {value}' for key, value in dict.items()
        )

        print(output_string)


iterateDictionary(students)
iterateDictionaryListComprehension(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


'''
    Create a function iterateDictionary2(key_name, some_list) that, given a list of 
    dictionaries and a key name, the function prints the value stored in that key for 
    each dictionary.
'''


def iterateDictionary2(key, list):
    for dict in list:
        print(dict[key])


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

'''
    Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints 
    the name of each key along with the size of its list, and then prints the associated values within 
    each key's list.
'''


def printInfo(dict):
    for list in dict.values():
        print(len(list))
        for item in list:
            print(item)


printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
