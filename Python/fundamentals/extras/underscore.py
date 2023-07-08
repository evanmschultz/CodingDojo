class Underscore:
    def map(self, iterable, callback):
        '''
            Creates new list of all the items in an iterable by running the passed in function 
            on each value and returns it in a new list so the method can work on multiple lists 
            and tuples.

            Example: map([1,2,3], lambda x: x * 2) output: [2, 4, 6]
        '''
        result = []
        for item in iterable:
            result.append(callback(item))
        return result

    def find(self, iterable, callback):
        '''
            Returns the first item in the iterable that matches the callback requirement

            Example: find([1,2,3], lambda x: x % 2 == 0) output: 2
        '''
        result = None
        for item in iterable:
            if callback(item):
                return item
        return result

    def filter(self, iterable, callback):
        '''
            Creates a new list of all the items in the original iterable that match the conditionals
            passed in by callback.

            Example: filter([1,2,3, 4], lambda x: x % 2 == 0) output: [2, 4]
        '''
        result = []
        for item in iterable:
            if callback(item):
                result.append(item)
        return result

    def reject(self, iterable, callback):
        '''
            Creates a new list of all the items in the original iterable that do not match the 
            conditionals passed in by callback.

            Example: reject([1,2,3, 4], lambda x: x % 2 == 0) output: [1, 3]
        '''
        result = []
        for item in iterable:
            if not callback(item):
                result.append(item)
        return result


if __name__ == '__main__':
    _ = Underscore()  # instantiate class with '_' as the variable name

    # tests map method
    result_1 = _.map([1, 2, 3, 4, 5, 6], lambda x: x *
                     2)  # output: [2, 4, 6, 8, 10, 12]
    print(result_1)
    # tests find method
    result_2 = _.find(result_1, lambda x: x > 9)  # output: 10
    print(result_2)
    # tests filter method
    result_3 = _.filter([1, 2, 3, 4, 5, 6], lambda x: x %
                        2 == 0)  # output: [2, 4, 6]
    print(result_3)
    # tests reject method
    result_4 = _.reject([1, 2, 3, 4, 5, 6], lambda x: x %
                        2 == 0)  # output: [1, 2, 3]
    print(result_4)
