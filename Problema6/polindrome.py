"""
Funcion que permite identificar si una frase/palabra es polindroma (se lee igual de izquierda a derecha que de derecha a izquierda)

Input: Frase/Palabra
Output: True si es polindroma, False en otro caso
    Salida en pantalla con mensaje informativo
"""


def isPolindrome(word):
    pol = word.upper().replace(" ", "")
    r = -1
    for i in pol:
        if i != pol[r]:
            return False
        r -= 1
    return True


def message(word):
    if isPolindrome(word):
        return f'La palabra "{word}" es polindroma'
    else:
        return f'La palabra "{word}" no es polindroma'


if __name__ == '__main__':
    word = input('Ingrese una palabra: ')
    print(message(word))
