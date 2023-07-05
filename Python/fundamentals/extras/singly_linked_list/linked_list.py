from node import Node


class List:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        '''
            O(1) time and space complexity
        '''
        # instantiate a new node with the value argument
        new_node = Node(value)
        # update new node's next_node to be current head
        new_node.next_node = self.head
        # update head to be new_node
        self.head = new_node

        # return self to allow for chaining
        return self

    def print_list_values(self):
        '''
            O(N) time complexity O(1) space complexity
        '''
        current_node = self.head

        if not current_node:
            print('Can\'t print values of an empty list')
            return self

        # while current_node is not None (there is a next_node attribute)
        while current_node:
            print(current_node.value)

            # update current_node to be its own next node
            current_node = current_node.next_node

        return self

    def add_to_tail(self, value):
        '''
            O(N) time complexity O(1) space complexity
        '''
        # instantiate a new node, its next_node = None
        new_tail = Node(value)
        # set next node variable to the head, this is our runner
        pointer = self.head
        # check if there is even a head
        if pointer:

            # move until you find the tail, the node with no pointer attribute
            while pointer.next_node:
                pointer = pointer.next_node

            # the old tail's pointer to the new tail
            pointer.next_node = new_tail
        else:
            # the list is empty, so the head and tail are both the new node
            self.head = new_tail

        return self

    def remove_from_head(self):
        # update head to be current head's next_node if head exists
        # because if the pointer is lost python will get rid of the Node using garbage collection
        if self.head:
            self.head = self.head.next_node
        # if the head doesn't exists do nothing

        return self

    def remove_from_tail(self):
        # if there is a head, and there is a next node loop through the list until the tail is found
        # update the second to last node's next_node attribute to be None
        if self.head and self.head.next_node:
            new_tail = self.head
            pointer = self.head.next_node

            # while the pointer has a next_node attribute
            while pointer.next_node:
                # update the new_tail to be the pointer
                new_tail = pointer
                # move pointer to the next_node
                pointer = new_tail.next_node

            # set the new tail's next_node pointer to be None
            new_tail.next_node = None
        else:
            self.head = None

        return self

    def remove_value(self, value, remove_all=False):
        # if there is no head, exit
        if not self.head:
            print('The list is already empty')
            return self

        # set counter for if remove_all is set to True
        counter = 0

        # Remove the head if it matches the target value until there
        # are no more sequential nodes match target
        while self.head and self.head.value == value:
            self.remove_from_head()

            # if we don't want to remove all of target value, exit
            if not remove_all:
                print(f'Value: {value} was removed from the list')
                return self
            counter += 1

        current_node = self.head
        while current_node and current_node.next_node:
            # If the next node's value matches target
            if current_node.next_node.value == value:
                # reassign node's next_node pointer by skipping the next node
                current_node.next_node = current_node.next_node.next_node

                # if we don't want to remove all of target value, exit
                if not remove_all:
                    print(f'Value: {value} was removed from the list')
                    return self
                counter += 1
            else:
                # move current_node to iterate through list
                current_node = current_node.next_node

        # If the tail's value matches, remove it
        if current_node and current_node.value == value:
            self.remove_from_tail()

        print(f'Value: {value} was removed from the list {counter} time(s)')
        return self

    def insert_at(self, value, n):
        # if n is 0 or negative, update head with node
        if n <= 0:
            self.add_to_head(value)
            return self

        # set current_node for loop
        current_node = self.head
        while current_node:
            # decrement n
            n -= 1

            # if position has been reached
            if n == 0:
                next_node = current_node.next_node
                current_node.next_node = Node(value, next_node)
                return self

            current_node = current_node.next_node

        # if n was larger than the length of the list add to tail
        self.add_to_tail(value)

        return self
