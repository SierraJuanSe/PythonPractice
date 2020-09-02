'''
Permite calcular el descuento de un producto segun el dia de la semana

Input: precio
Input: dia de la semana lunes: l, martes: m, miercoles M, jueves: j, viernes: v, sabado: s, domingo: d.
Output: descuento
'''

DISCOUNT_VALUES = {
    'l': 0.1,
    'm': 0.05,
    'M': 0.03,
    'j': 0.01,
    'v': 0.07,
    's': 0,
    'd': 0.01
}


def calcDisc(price, day):
    global DISCOUNT_VALUES
    return price * DISCOUNT_VALUES.get(day, 0)


def message(price, day):
    disc = calcDisc(price, day)
    return f'valor descuento: {disc}, total a pagar: {price-disc}'


if __name__ == '__main__':
    price = float(input('Ingrese el precio: '))
    day = input('Ingrese el dia de la semana (l,m,M,j,v,s,d): ')
    print(message(price, day))
