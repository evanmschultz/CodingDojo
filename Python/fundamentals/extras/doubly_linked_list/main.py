from linked_list import List

'''
    write tests for the List class
'''
# instantiate a new list
test_list = List()
# add a list
test_list.add_to_head(1).add_to_tail(2).add_to_tail(3).add_to_head(0)
# print the list's values
test_list.print_list()
print('testing remove_head')
test_list.remove_head().remove_head().remove_head().remove_head().remove_head()
# add to list
test_list.add_to_head(1).add_to_tail(2).add_to_tail(3).add_to_head(0)
test_list.print_list()
print('Testing remove_tail')
test_list.remove_tail().remove_tail().remove_tail().remove_tail().remove_tail()
# add to list
test_list.add_to_head(1).add_to_tail(2).add_to_tail(3).add_to_head(0)
test_list.print_list()
print('Testing insert_at')
test_list.insert_at(4, 4).print_list()
test_list.insert_at(-1, 0).print_list()
test_list.insert_at('test', 2).print_list()

# confirming length is a list attribute not a class attribute
test_list_2 = List()
print(test_list.length)
print(test_list_2.length)
