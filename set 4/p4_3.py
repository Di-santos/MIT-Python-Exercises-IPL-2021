def euclid_mdc(n1, n2):
    if n1<0:
        n1 = n1 * -1
    if n2<0:
        n2 = n2 * -1

    if n1==0:
        return n2
    if n2==0:
        return n1

    if n1 < n2:
        return euclid_mdc(n1, n2 - n1)

    elif n1 > n2:
        return euclid_mdc(n1 - n2, n1)

    return n1

class Rational():
    def __init__(self, num, denomin):
        self.num = num
        self.denomin = denomin
    
    def get_numerator(self):
        return int(self.num)

    def get_denominator(self):
        return int(self.denomin)
    
    def to_float(self):
        return float(self.num / self.denomin)

    def reciprocal(self):
        return Rational(self.denomin, self.num)
    
    def reduce(self):
        mdc = euclid_mdc(self.num, self.denomin)
        return Rational(self.num / mdc, self.denomin / mdc)     
    
    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.num * other.denomin + self.denomin * other.num, self.denomin * other.denomin).reduce()
            
        elif isinstance(other, int):
            return Rational(self.denomin * other + self.num, self.denomin).reduce()

        elif isinstance(other, float):
            return (self.num / self.denomin) + other
        
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.num * other.num, self.denomin * other.denomin).reduce()
            
        elif isinstance(other, int):
            return Rational(self.num * other, self.denomin).reduce()
            
        elif isinstance(other, float):
            return self.to_float() * other
        
        else:
            return None
    
    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.num * other.denomin, self.denomin * other.num).reduce()
            
        elif isinstance(other, int):
            if other != 0:
                return Rational(self.num / other, self.denomin).reduce()
            
            elif other == 0:
                return 0

        elif isinstance(other, float):
            return (self.num / self.denomin) + other
        
        else:
            return None

    def __sub__(self, other):
        if isinstance(other, Rational):
            cross_novo_num = self.num * other.denomin - self.denomin * other.num
            return Rational(cross_novo_num, self.denomin * other.denomin).reduce()
            
        elif isinstance(other, int):
            return Rational(self.num - self.denomin * other, self.denomin).reduce()

        elif isinstance(other, float):
            return (self.num / self.denomin) - other
        
        else:
            return None 
