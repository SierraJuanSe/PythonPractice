"""
Genera la siguiente serie de numeros donde n es ingresado por el usuario
1
22
333
444
....
N veces N

Input : N, numero entero
Output: serie
"""


def numPyramid(N):
    for i in range(1, N+1):
        print(f'{i}'*i)


if __name__ == '__main__':
    N = int(input('Ingrese un numero entero: '))
    print('Serie generada: ')
    numPyramid(N)
