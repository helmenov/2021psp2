# mymodule3.py

def gcd(p,q):
    """pとqとの最大公倍数
    """
    while p % q != 0:
        old_p = p
        old_q = q
        p = old_q
        q = old_p % old_q
    
    return q

class Rational():
    def __init__(self,num,den = 1):
        Ngcd = gcd(num,den)
        self.num = int(num/Ngcd)
        self.den = int(den/Ngcd)

    def __str__(self):
        return str(self.num) + '/' + str(self.den)
    
    def __add__(self,arg1):
        den = self.den * arg1.den
        num = self.num * arg1.den + arg1.num * self.den
        return Rational(num,den)
