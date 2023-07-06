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
        for _ in range(length):
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
            loop. Worst case is ~n^2/2. Space complexity is O(1).

            Update: Improves selection sort by using two pointers and a maximum variable.
            Time and space complexity stay the same as the standard selection sort, because
            worst case, meaning the first time the inner loop runs, it runs n times. Since
            we don't calculate constants in Big O notation, it is stile n^2

            Returns:
                The list.
        '''  # /////////////////////////////////////////////////////////

        # set counter to check time complexity
        counter = 0
        # set left and right pointers
        left, right = 0, len(self.list) - 1

        while left < right:
            # set min, max, and their indexes
            # set min, max in loop, because they will change each time this outer loop runs
            minimum = self.list[left]
            min_index = left
            maximum = self.list[right]
            max_index = right

            # loop from left to right pointers
            for i in range(left, right + 1):
                # update counter
                counter += 1
                # update min if current num is less than min, update min_index
                if self.list[i] < minimum:
                    minimum = self.list[i]
                    min_index = i

                # update max if current num is larger than max, update max_index
                if self.list[i] > maximum:
                    maximum = self.list[i]
                    max_index = i

            # swap min and list[left], will swap with self if min was list[i]
            print(f'Swapping {self.list[left]} and {minimum}')
            self.list[min_index], self.list[left] = self.list[left], self.list[min_index]

            # swap max and list[right], will swap with self if max was list[i]
            print(f'Swapping {self.list[left]} and {maximum}')
            self.list[max_index], self.list[right] = self.list[right], self.list[max_index]

            # move pointers
            left, right = left + 1, right - 1

        print(f'{self.list}\n\nAlgorithm ran {counter} times')
        return self


if __name__ == '__main__':
    # instantiate class
    list = SortClass()
    # generate random list
    print('\n', '/ ' * 20, ' Generating random list  ', '/ ' * 20, '\n')
    list.generate_rand_list(1000, 10000).print_list()
    # start sort method
    print('\n', '/ ' * 20, ' Selection Sort  ', '/ ' * 20, '\n')
    list.selection_sort()
    print('\n', '/ ' * 20, ' Sort complete  ', '/ ' * 20, '\n')
