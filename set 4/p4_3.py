class Rational():
    def __init__(self, num, denomin):
        self.num = num
        self.denomin = denomin
    
    def get_numerator(self):
        return int(self.num)

    def get_denominator(self):
        return int(self.denomin)
    
    def to_float(self):
        return self.num / self.denomin

    def reciprocal(self):
        return Rational(self.denomin, self.num)
    
    def reduce(self):
        def euclid_mdc(n1, n2):
            while n1 != 0:
                if n1 < n2:
                    aux = n1
                    n1 = n2
                    n2 = aux
                
                n1-= n2
                
            return n2

        mdc = euclid_mdc(self.num, self.denomin)

        return Rational(self.num/mdc, self.denomin/mdc)     
    
    def __add__(self, other):
        if
    
    def __mul__(self, other):
    
    def __truediv__(self, other):
    
    def __sub__(self, other):


'''
def get_gcd(a, b):
    """Computes greatest common divisor between ints a,b"""
    # Segue os passos do algoritmo em https://sites.math.rutgers.edu/~greenfie/gs2004/euclid.html
    if a < b:
        a, b = b, a

    while True:
        r = a % b
        if r == 0:
            return b

        a, b = b, r


class Rational:
    def __init__(self, num, den):
        self.num = int(num)
        self.den = int(den)

    def get_numerator(self):
        return self.num

    def get_denominator(self):
        return self.den

    def to_float(self):
        return self.num / self.den

    def reciprocal(self):
        return Rational(self.den, self.num)

    def reduce(self):
        gcd = get_gcd(self.num, self.den)  # mÃ¡ximo divisor comum

        return Rational(self.num / gcd, self.den / gcd)

    # As operaÃ§Ãµes abaixo sÃ£o as operaÃ§Ãµes bÃ¡sicas de fraÃ§Ãµes
    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.num * other.den + self.den * other.num, self.den * other.den).reduce()

        if isinstance(other, int):
            return Rational(self.num + self.den * other, self.den).reduce()

        if isinstance(other, float):
            return self.to_float() + other

        return None

    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.num * other.den - self.den * other.num, self.den * other.den).reduce()

        if isinstance(other, int):
            return Rational(self.num - self.den * other, self.den).reduce()

        if isinstance(other, float):
            return self.to_float() - other

        return None

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.num * other.num, self.den * other.den).reduce()

        if isinstance(other, int):
            return Rational(self.num * other, self.den).reduce()

        if isinstance(other, float):
            return self.to_float() * other

        return None

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.num * other.den, self.den * other.num).reduce()

        if isinstance(other, int):
            return Rational(self.num, self.den * other).reduce()

        if isinstance(other, float):
            return self.to_float() / other

        return None '''