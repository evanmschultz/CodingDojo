from linked_list import List

# instantiate list
list = List()

print('Removing from head and tail when list is empty')
list.remove_from_head().remove_from_tail()

print('\nAdding tail to empty list')
# update tail, since list is empty, it will set it as the head
list.add_to_tail('tail').print_list_values()

print('\nRemoving head when there is only one node in the linked list')
list.remove_from_head().print_list_values()

print('\nRemoving tail when the list is empty, then when it has only one node')
list.remove_from_tail().add_to_head(
    'temp head').print_list_values().remove_from_tail().print_list_values()

print('\nSetting head')
# set initial head and print
list.add_to_head('head').print_list_values()

print('\nAdding to head')
# update head and print values
list.add_to_head('new head').print_list_values()

print('\nAdding new tail and printing')
# update tail and print values
list.add_to_tail('new tail').print_list_values()

print('\nRemoving from head')
list.remove_from_head().print_list_values()

print('\nPrint current list')
list.print_list_values()

print('\nRemoving from tail')
list.remove_from_tail().print_list_values()

print('\nRemoving from tail when there is only one node in list')
list.remove_from_tail().print_list_values()

print('\nLonger tests, adding and removing 5 from tail')
list.add_to_tail('1').add_to_tail('2').add_to_tail('3').add_to_tail('4').add_to_tail(
    '5').print_list_values().remove_from_tail().print_list_values().remove_from_tail(
).print_list_values().remove_from_tail().print_list_values().remove_from_tail().print_list_values().remove_from_tail().print_list_values()

print('\nCompleted longer test\n')
list.print_list_values()
print('\n')

print('Testing remove_value')
list.add_to_head(1)
list.remove_value(1)
print('\n1) remove value 1')
list.print_list_values
print('\n2) adding and printing')
list.add_to_head(2).add_to_head(
    1).remove_value(2).remove_value(3).print_list_values()
list = List()
print('\nTesting remove all instances of the value from the list')
list.print_list_values()
list.add_to_tail(2).add_to_tail(
    1).add_to_head(2).add_to_head(3).add_to_tail(2)
list.remove_value(1, True)
print('\nprinting list')
list.print_list_values()
list.remove_value(2, True).add_to_tail(
    3).add_to_tail(1).add_to_tail(1).add_to_tail(3).add_to_tail(1).add_to_tail(3)
list.print_list_values()
print('\n')
list.remove_value(3, True)
list.print_list_values()
list.remove_value(1, True).print_list_values()
list.add_to_head(1).print_list_values().remove_value(1).print_list_values()
list.remove_value(1)

print('\ntesting insert_at')
list.add_to_head(1).add_to_tail(2).add_to_tail(3).print_list_values()
print('\nList built above, now testing insert_at')
list.insert_at(5, 2).print_list_values()
