import unittest

from functions import reverse_list, is_palindrome, coins, factorial, fibonacci


class ReverseIterableTest(unittest.TestCase):
    '''
        Tests to check the reverse_list function
    '''

    def testOne(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])

    def testTwo(self):
        self.assertEqual(
            reverse_list(['one', 'two', 'three']), ['three', 'two', 'one'])

    def testThree(self):
        self.assertEqual(reverse_list([1, {'key': 'value'}, [1, 2, 3]]), [
                         [1, 2, 3], {'key': 'value'}, 1])

    def testFour(self):
        self.assertEqual(reverse_list([1, 2]), [2, 1])

    # runs before any tests
    def setUp(self):
        print(f'\nRunning setUp for reverse_list\n')

    # runs after all tests
    def tearDown(self):
        print(f'\n\nRunning tearDown for reverse_list\n{"/  " * 30}')


class IsPalindromeTests(unittest.TestCase):
    '''
        Tests to check the is_palindrome function
    '''

    def testOne(self):
        self.assertTrue(is_palindrome('Race car'))

    def testTwo(self):
        self.assertFalse(is_palindrome('Race cr'))

    def testThree(self):
        self.assertFalse(is_palindrome('Race a car'))

    def testFour(self):
        self.assertTrue(is_palindrome('hannah'))

    def testFive(self):
        self.assertTrue(is_palindrome('A man, a plan, a canal: Panama'))

    def testSix(self):
        self.assertTrue(is_palindrome('  '))

    # runs before any tests
    def setUp(self):
        print(f'\nRunning setUp for is_palindrome\n')

    # runs after all tests
    def tearDown(self):
        print(f'\n\nRunning tearDown for is_palindrome\n{"/  " * 30}')


class CoinsTests(unittest.TestCase):
    '''
        Tests to check coins function
    '''

    def testOne(self):
        self.assertEqual(coins(23), [0, 2, 0, 3])

    def testTwo(self):
        self.assertEqual(coins(0), [0, 0, 0, 0])

    def testThree(self):
        self.assertEqual(coins(99), [3, 2, 0, 4])

    def testFour(self):
        self.assertEqual(coins(60), [2, 1, 0, 0])

    def testFive(self):
        self.assertEqual(coins(9), [0, 0, 1, 4])

    def testSix(self):
        self.assertEqual(coins(101), [0, 0, 0, 1])

    # runs before any tests
    def setUp(self):
        print(f'\nRunning setUp for coins\n')

    # runs after all tests
    def tearDown(self):
        print(f'\n\nRunning tearDown for coins\n{"/  " * 30}')


class FactorialTests(unittest.TestCase):
    '''
        Tests to check factorial function
    '''

    def testOne(self):
        self.assertEqual(factorial(5), 120)

    def testTwo(self):
        self.assertEqual(factorial(0), 1)

    def testThree(self):
        self.assertEqual(factorial(10), 3628800)

    def testFour(self):
        self.assertEqual(factorial(1), 1)

    def testFive(self):
        self.assertEqual(factorial(12), 479001600)

    def testSix(self):
        self.assertEqual(factorial(-1), None)

    # runs before any tests

    def setUp(self):
        print(f'\nRunning setUp for coins\n')

    # runs after all tests
    def tearDown(self):
        print(f'\n\nRunning tearDown for coins\n{"/  " * 30}')


class FibonacciTest(unittest.TestCase):
    '''
        Tests to check fibonacci function
    '''

    def testOne(self):
        self.assertEqual(fibonacci(5), 5)

    def testTwo(self):
        self.assertEqual(fibonacci(0), 0)

    def testThree(self):
        self.assertEqual(fibonacci(10), 55)

    def testFour(self):
        self.assertEqual(fibonacci(1), 1)

    def testFive(self):
        self.assertEqual(fibonacci(12), 144)


if __name__ == "__main__":
    unittest.main()  # run tests
