# mymodule6.py

import mymodule4 as my

class RationalChild(my.Rational):
    def __str__(self):
        return str(self.num) + '÷' + str(self.den)

    def show(self):
        print('分子=' , self.num)
        print('分母=', self.den)
