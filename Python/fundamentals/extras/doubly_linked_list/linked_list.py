from node import Node


class List:
    length = 0

    def __init__(self):
        self.head = None
        self.tail = None

    ''' # /////////////////////////////////////////////////////////
                            Add to head method
    '''  # /////////////////////////////////////////////////////////

    def add_to_head(self, value):
        # create new node with head as its next_node
        new_head = Node(value, self.head)
        # update the head's prev_node to be the new node
        if self.head:
            self.head.prev_node = new_head
        # update the list's head
        self.head = new_head
        # update the list's tail if it's empty
        if not self.tail:
            self.tail = new_head

        # update the list's length
        self.length += 1

        return self

    ''' # /////////////////////////////////////////////////////////
                            Add to tail method
    '''  # /////////////////////////////////////////////////////////

    def add_to_tail(self, value):
        # create new node with no next_node and the tail as its prev_node
        new_tail = Node(value, None, self.tail)
        # update the tail's next_node to be the new node
        if self.tail:
            self.tail.next_node = new_tail
        # update the list's tail
        self.tail = new_tail
        # update the list's head if it's empty
        if not self.head:
            self.head = new_tail

        # update the list's length
        self.length += 1

        return self

    ''' # /////////////////////////////////////////////////////////
                            Remove head method
    '''  # /////////////////////////////////////////////////////////

    def insert_at(self, value, index):
        # if the location is 0 or less, add to head
        if index <= 0:
            self.add_to_head(value)
            return self
        # if the location is beyond the end of the list, add to tail
        if index >= self.length:
            self.add_to_tail(value)
            return self

        # set runner to head
        runner = self.head
        # loop while runner exists
        while runner:
            # decrement index
            index -= 1

            # if index equals 0 update surrounding nodes
            if index == 0:
                # store the new node's next_node in a variable
                next_node = runner.next_node.next_node
                # set runner's next node
                runner.next_node = Node(value, next_node, runner)
                # update next_node's previous node
                next_node.prev_node = runner.next_node
                # update length
                self.length += 1

                return self
            # move runner
            runner = runner.next_node

    ''' # /////////////////////////////////////////////////////////
                            Remove head method
    '''  # /////////////////////////////////////////////////////////

    def remove_head(self):
        # if no head exists print empty
        if not self.head:
            print('The list is already empty')
            return self
        # if there is 1 node in the list update head and tail to None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            new_head = self.head.next_node
            # update the new head's previous node to None
            new_head.prev_node = None
            # update head to be next node
            self.head = new_head

        self.length -= 1
        return self

    ''' # /////////////////////////////////////////////////////////
                            Remove tail method
    '''  # /////////////////////////////////////////////////////////

    def remove_tail(self):
        # if no tail exists print empty
        if not self.tail:
            print('The list is already empty')
            return self
        # if there is only 1 node in the list set tail and head to None
        if self.tail == self.head:
            self.tail = None
            self.head = None
        else:
            new_tail = self.tail.prev_node
            # update the new tail's next node to None
            new_tail.next_node = None
            # update tail to new_tail
            self.tail = new_tail
        self.print_list()
        self.length -= 1
        return self

    ''' # /////////////////////////////////////////////////////////
                            Print list method
    '''  # /////////////////////////////////////////////////////////

    def print_list(self):
        # set a runner to the head
        runner = self.head
        print_list = []

        # while the runner is not None
        while runner:
            # print the runner's value
            print_list.append(runner.value)
            # update the runner to be its own next_node
            runner = runner.next_node

        print(print_list)
        return self
