import unittest
from fizzbuzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def test_simple_should_return_the_number(self):
        self.assertEqual(fizz_buzz(1), 1)
        self.assertEqual(fizz_buzz(2), 2)
        self.assertEqual(fizz_buzz(4), 4)

    def test_multiple_3_should_return_fizz(self):
        self.assertEqual(fizz_buzz(3), "Fizz")
        self.assertEqual(fizz_buzz(9), "Fizz")

    def test_multiple_5_should_return_buzz(self):
        self.assertEqual(fizz_buzz(5), "Buzz")
        self.assertEqual(fizz_buzz(10), "Buzz")

    def test_multiple_3_and_5_should_return_fizzbuzz(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz")
        self.assertEqual(fizz_buzz(30), "FizzBuzz")
