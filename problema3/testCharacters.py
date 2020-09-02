import unittest

import characters


class testCharacters(unittest.TestCase):

    def test_FirstLastChar(self):
        word = 'Programacion'
        self.assertEqual(characters.firstLastChar(
            word), ('P', 'n'), f'La palabra es {word}')

    def test_message(self):
        word = 'Programacion'
        sol = 'Primer caracter: P, Ultimo caracter: n'
        self.assertEqual(characters.message(
            word), sol, f'La palabra es {word}')


if __name__ == '__main__':
    unittest.main()
