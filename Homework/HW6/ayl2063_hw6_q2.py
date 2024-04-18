from DoublyLinkedList import DoublyLinkedList

class Integer:
    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        for i in range(len(num_str)):
            self.data.add_last(int(num_str[i]))
        while self.data.header.next.data == 0 and len(self.data) > 1:
            self.data.delete_first()

    def __add__(self, other):
        sum = Integer('')
        if other.data.is_empty():
            return self
        if self.data.is_empty():
            return other
        if len(self.data) > len(other.data):
            curr1, curr2 = self.data.trailer.prev, other.data.trailer.prev
        else:
            curr1, curr2 = other.data.trailer.prev, self.data.trailer.prev
        carry = 0
        while curr1.prev is not None and curr2.prev is not None:
            num1, num2 = curr1.data, curr2.data
            temp = num1 + num2 + carry
            carry = temp // 10
            if carry > 0:
                temp = temp % 10
            sum.data.add_first(temp)
            curr1, curr2 = curr1.prev, curr2.prev
        for i in range(abs(len(self.data) - len(other.data))):
            temp = curr1.data + carry
            carry = temp // 10
            if carry > 0:
                temp %= 10
            sum.data.add_first(temp)
            curr1 = curr1.prev
        if carry > 0:
            sum.data.add_first(carry)
        while sum.data.header.next.data == 0 and len(sum.data) > 1:
            sum.data.delete_first()
        return sum

    def __mul__(self, other):
        product = Integer('')
        if len(self.data) > len(other.data):
            long, short = self.data, other.data         
        else:
            long, short = other.data, self.data
        short_curr = short.trailer.prev
        carry = 0
        for i in range(len(short)):
            t = Integer('')
            long_curr = long.trailer.prev
            for j in range(len(long)):
                temp = long_curr.data * short_curr.data + carry
                carry = temp // 10
                if carry > 0:
                    temp %= 10
                t.data.add_first(temp)
                long_curr = long_curr.prev
            for x in range(i):
                t.data.add_last(0)
            product = product + t 
            short_curr = short_curr.prev
        if carry > 0:
            product.data.add_first(carry)
        while product.data.header.next.data == 0 and len(product.data) > 1:
            product.data.delete_first()
        return product

    def __repr__(self):
        s = ''
        for i in self.data:
            s += str(i)
        return s

def main():
    a = Integer('0')
    b = Integer('62')
    c = a * b
    print(c)

#main()