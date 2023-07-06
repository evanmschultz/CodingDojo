import random


class SortClass:
    def __init__(self):
        self.list = []

    def generate_rand_list(self, length, max_num):
        ''' # /////////////////////////////////////////////////////////
            Generates a list of random numbers, with bounds +/- |max_num|, 
            with len of the length arg.

            Returns:
                The list.
        '''  # /////////////////////////////////////////////////////////

        # clear list
        self.list.clear()
        # loop over length, '_' is a convention of showing that the variable won't be used in the loop
        for _ in range(length + 1):
            # append a random number to the list within the given bound
            self.list.append(random.randint(-max_num, max_num))

        return self

    def print_list(self):

        print(self.list)
        return self

    def selection_sort(self):
        ''' # /////////////////////////////////////////////////////////
            Sorts the list in place in ascending order using the selection 
            sort algorithm. Time complexity O(n^2). The outer loop runs n times
            and the inner loop runs n-i times, where i is the iteration of the outer
            loop. Worst case is ~n^2/2.

            Returns:
                The list.
        '''  # /////////////////////////////////////////////////////////

        # set counter to check time complexity
        counter = 0
        # loop over list
        for i in range(len(self.list)):
            # set min in loop, because it will change each time this loops, update to next lowest index
            min = self.list[i]
            min_index = i
            for j in range(i, len(self.list)):
                # update counter
                counter += 1
                # update min if current num is less than min, update min_index
                if self.list[j] < min:
                    min = self.list[j]
                    min_index = j
            # swap min and list[i], will swap with self if min was list[i]
            print(f'Swapping {self.list[i]} and {min}')
            self.list[min_index], self.list[i] = self.list[i], self.list[min_index]

        print(f'{self.list}\n\nAlgorithm ran {counter} times')
        return self


if __name__ == '__main__':
    # instantiate class
    list = SortClass()
    # generate random list
    print('\n', '/ ' * 20, ' Generating random list  ', '/ ' * 20, '\n')
    list.generate_rand_list(100, 1000).print_list()
    # start sort method
    print('\n', '/ ' * 20, ' Selection Sort  ', '/ ' * 20, '\n')
    list.selection_sort()
    print('\n', '/ ' * 20, ' Sort complete  ', '/ ' * 20, '\n')
