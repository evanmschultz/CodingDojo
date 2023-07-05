class MathDojo:
    def __init__(self):
        self.result = 0

    # use the splat operator to make a tuple (iterable) of all the arbitrarily large amount of arguments
    def add(self, *nums):
        # check if at least one argument was passed in, could use (self, num, *nums) as parameters but then
        # it will return a type error for missing positional arguments
        if len(nums) < 1:
            print('Pass in at least 1 number to add')

            return self

        # iterate over all the arguments and add them to the result attribute
        for num in nums:
            self.result += num
        # print the temp result
        print(f'The current sum: {self.result}')

        return self

    # see comments for the add method
    def subtract(self, *nums):
        if len(nums) < 1:
            print('Pass in at least 1 number to subtract')

            return self

        for num in nums:
            self.result -= num
        # print the temporary result
        print(f'The current difference: {self.result}')

        return self


math_dojo = MathDojo()

x = math_dojo.add().add(1, 2, 3).subtract().subtract(3, 4).result

print(x)
