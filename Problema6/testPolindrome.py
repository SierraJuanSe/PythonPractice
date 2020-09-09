import unittest

import polindrome


class TestPolindrome(unittest.TestCase):
    def testPol(self):
        word = 'reconocer'
        self.assertTrue(polindrome.isPolindrome(word), 'Is polindrome')
        word = 'nombre'
        self.assertFalse(polindrome.isPolindrome(word), 'Is not polindrome')

    def testMessage(self):
        word = 'reconocer'
        message = f'La palabra {word} es polindroma'
        self.assertEqual(message, polindrome.message(word))
        word = 'nombre'
        message = f'La palabra {word} no es polindroma'
        self.assertEqual(message, polindrome.message(word))


if __name__ == '__main__':
    unittest.main()
