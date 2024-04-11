class Polynomial:
    def __init__(self, coefficients = [0]):
        self.coefficients = coefficients
    
    def __add__(self, other):
        if len(self.coefficients) < len(other.coefficients):
            temp = other.coefficients[:]
            result = Polynomial(temp)
            for i in range(len(self.coefficients)):
                result.coefficients[i] += self.coefficients[i]
        else:
            temp = self.coefficients[:]
            result = Polynomial(other)
            for i in range(len(other.coefficients)):
                result[i] += other.coefficients[i]           
        return result

    def __call__(self, param):
        x = 0
        for i in range(len(self.coefficients)):
            x += self.coefficients[i] * (param ** i)
        return x

    def derive(self):
        self.coefficients.pop(0)
        for i in range(len(self.coefficients)):
            self.coefficients[i] = self.coefficients[i] * i

    def __repr__(self):
        a, b = '',''
        if self.coefficients[0] != 0:
            b += ' + ' + str(self.coefficients[0])
        if self.coefficients[1] != 0:
            a += ' + ' + str(self.coefficients[1]) + 'x'
        s = a + b
        for i in range(2, len(self.coefficients)):
            plus = ' + '
            temp = self.coefficients[i]
            if self.coefficients[i] < 0:
                plus = ' - '
                temp *= -1
            if self.coefficients[i] != 0:
                s = plus + str(temp) + 'x^' + str(i) + s
        return s[3:]
    
def main():
    p1 = Polynomial([3, 7, 1, -9, 2])
    p2 = Polynomial([0, 9, 0, 0, 0,0,0,0,0,3])
    p3 = p1 + p2
    p4 = Polynomial([0,1,2])
    p5 = p4(1)
    print(p1)
    print(p2)
    print(p3)
    print(p5)
    p1.derive()
    print(p1)
    
main()