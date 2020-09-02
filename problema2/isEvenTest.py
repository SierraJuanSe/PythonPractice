import unittest

import isEven


class TestProblem2(unittest.TestCase):

    def test_isEven(self):
        self.assertEqual(isEven.is_even(2), True, 'Debe ser True')
        self.assertEqual(isEven.is_even(5), False, 'Debe ser False')

    def test_message(self):
        num = 2
        self.assertEqual(isEven.main(num), f'El numero {num} es par', 'es par')
        num = 5
        self.assertEqual(isEven.main(
            num), f'El numero {num} no es par', 'no es par')


if __name__ == '__main__':
    unittest.main()
