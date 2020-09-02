'''
Permite imprimir de una palabra el primer y ultimo caracter.

Input: Palabra (Str)
Output: mensaje sobre el primer y ultimo caracter de la palabra
'''


def firstLastChar(word):
    return (word[0], word[-1])


def message(word):
    chars = firstLastChar(word)
    return f'Primer caracter: {chars[0]}, Ultimo caracter: {chars[1]}'


if __name__ == '__main__':
    word = input('Ingrese una palabra: ')
    print(message(word))
