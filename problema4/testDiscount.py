import unittest

import discount


class TestDiscount(unittest.TestCase):

    def test_calcDisc(self):
        price = 100
        day = ['l', 'm', 'M', 'j', 'v', 's', 'd']
        self.assertEqual(discount.calcDisc(
            price, day[0]), price*0.1, 'el descuento debe ser de 10')

    def test_message(self):
        price = 100
        day = ['l', 'm', 'M', 'j', 'v', 's', 'd']
        sol = f'valor descuento: 10, total a pagar: 90'
        self.assertEqual(discount.message(price, day[0]), sol, sol)
