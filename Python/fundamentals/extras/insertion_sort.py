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

    def insertion_sort(self):
        ''' # /////////////////////////////////////////////////////////
            Sorts a list using the insertion sort algorithm. It has O(n^2)time complexity, but performs 
            better on average compared to selection sort, even with two pointers. If the list is nearly
            sorted it performs less checks. Space complexity is O(1)

            Returns:
                The list.
        '''  # /////////////////////////////////////////////////////////

        # set counter to see effectiveness in action
        counter = 0

        # loop over array, outer
        for i in range(1, len(self.list)):
            # set variable index to loop down to start of list
            index = i

            # loop until you get to the first item of the list, index is > 0 because we are comparing to (index - 1)
            while index > 0 and self.list[index] < self.list[index - 1]:
                # swap values so the smaller number goes down and larger goes up
                self.list[index], self.list[index -
                                            1] = self.list[index - 1], self.list[index]
                # decrement index, increment counter
                index -= 1
                counter += 1

        print(f'{self.list}\n\nAlgorithm took {counter} loops')

        return self


if __name__ == '__main__':
    # instantiate class and create list
    list = SortClass()
    print('\n', '/ ' * 20, ' Generating random list  ', '/ ' * 20, '\n')
    list.generate_rand_list(10, 100).print_list()
    print('\n', '/ ' * 20, ' Running insertion sort  ', '/ ' * 20, '\n')
    # run sort
    list.insertion_sort()
    print('\n', '/ ' * 20, ' Insertion sort complete  ', '/ ' * 20, '\n')
