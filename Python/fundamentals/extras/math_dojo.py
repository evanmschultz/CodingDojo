import unittest


class MathDojo:
    def __init__(self):
        self.result = 0

    # use the splat operator to make a tuple (iterable) of all the arbitrarily large amount of arguments
    def add(self, *nums):
        # check if at least one argument was passed in, could use (self, num, *nums) as parameters but then
        # it will return a type error for missing positional arguments
        if len(nums) < 1:
            return 'Pass in at least 1 number to add'

        # iterate over all the arguments and add them to the result attribute
        for num in nums:
            self.result += num
        # print the temp result
        print(f'The sum: {self.result}')

        return self.result

    # see comments for the add method
    def subtract(self, *nums):
        if len(nums) < 1:
            print('Pass in at least 1 number to subtract')

            return 'Pass in at least 1 number to subtract'
        self.result += nums[0]
        for i in range(1, len(nums)):
            self.result -= nums[i]
        # print the temporary result
        print(f'The difference: {self.result}')

        return self.result


class AddTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(MathDojo().add(1, 2, 3), 6)

    def testTwo(self):
        self.assertEqual(MathDojo().add(2, -3), -1)

    def testThree(self):
        self.assertEqual(MathDojo().add(),
                         'Pass in at least 1 number to add')

    # runs before any tests
    def setUp(self):
        print(f'\nRunning setUp for add()\n')

    # runs after all tests
    def tearDown(self):
        print(f'\n\nRunning tearDown for add()\n{"/  " * 30}')


class SubtractTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(MathDojo().subtract(1, 2, 3), -4)

    def testTwo(self):
        self.assertEqual(MathDojo().subtract(2, -3), 5)

    def testThree(self):
        self.assertEqual(MathDojo().subtract(),
                         'Pass in at least 1 number to subtract')

    # runs before any tests
    def setUp(self):
        print(f'\nRunning setUp for subtract()\n')

    # runs after all tests
    def tearDown(self):
        print(f'\n\nRunning tearDown for subtract()\n{"/  " * 30}')


if __name__ == "__main__":
    unittest.main()
