class UnsignedBinaryInteger:
    def __init__(self, num_str):
        self.num = num_str
    
    def __lt__(self, other):
        if len(self.num) == len(other.num):
            for i in range(len(self.num)):
                if self.num[i] < other.num[i]:
                    return True
            return False
        else:
            return len(self.num) < len(other.num)
    
    def __gt__(self, other):
        return other < self
    
    def __eq__(self, other):
        return not self < other and not other < self
    
    def is_twos_power(self):
        count = 0
        for i in self.num:
            if i == 1:
                count += 1
        return count == 1 
    
    def largest_twos_power(self):
        return 2 ** (len(self.num) - 1)
    
    def __repr__(self):
        return '0b' + self.num
    
def main():
    i = UnsignedBinaryInteger('1101')
    i2 = i.largest_twos_power()
    print(i2)

main()