'''
Se necesita una solucion de software que le permita a un usuario conocer si un numero es par o no.

Input: numero entero
Output: Bool, indicando si un numero es par o no, Salida en pantalla con mensaje informativo
'''


def is_even(num):
    return True if num % 2 == 0 else False


def main(num):
    flag = is_even(num)
    if flag:
        print(f'El numero {num} es par')
    else:
        print(f'El numero {num} no es par')


if __name__ == '__main__':
    num = int(input('Ingresa un numero: '))
    main(num)
