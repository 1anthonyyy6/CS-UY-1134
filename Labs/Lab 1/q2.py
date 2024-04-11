class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        newCom = Complex(a, b)
        return newCom
    
    def __sub__(self, other):
        a = self.a - other.a
        b = self.b - other.b
        newCom = Complex(a,b)
        return newCom
    
    def __mul__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        resultA = a * c - b * d
        resultB = b * c + a * d
        result = Complex(resultA, resultB)
        return result
    
    def __iadd__(self, other):
        self.a += other.a
        self.b += other.b
        return self
    
    def __repr__(self):
        op = ' + '
        b = self.b
        if self.b < 0:
            op = ' - '
            b *= -1
        return str(self.a) + op + str(b) +'i'
    
def main():
    cplx1 = Complex(5, 2)
    print(cplx1)

    cplx2 = Complex(3,3)
    print(cplx2)

    print(cplx1 + cplx2)

    print(cplx1 - cplx2)

    print(cplx1 * cplx2)

    print(cplx1)
    print(cplx2)
main()