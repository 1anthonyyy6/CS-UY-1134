from DoublyLinkedList import DoublyLinkedList

class CompactString:
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        for i in range(len(orig_str)):
            if i > 0 and self.data.trailer.prev.data[0] == orig_str[i]:
                    self.data.trailer.prev.data = (orig_str[i], self.data.trailer.prev.data[1] + 1)
            else:
                self.data.add_last((orig_str[i], 1))

    def __add__(self, other):
        res = CompactString('')
        for i in self.data:
            res.data.add_last(i)
        for i in other.data:
            res.data.add_last(i)
        return res

    def __lt__(self, other):
        curr1 = self.data.header.next
        curr2 = other.data.header.next
        count1, count2 = curr1.data[1], curr2.data[1]
        while curr1.data is not None and curr2.data is not None:
            if curr1.data[0] == curr2.data[0]:
                count1 -= 1
                count2 -= 1
                if count1 == 0:
                    curr1 = curr1.next
                    if curr1.data is not None:
                        count1 = curr1.data[1]
                if count2 == 0:
                    curr2 = curr2.next
                    if curr2.data is not None:
                        count2 = curr2.data[1]
            elif curr1.data[0] > curr2.data[0]:
                return False
            else:
                return True
        return False

    def __le__(self, other):
        if len(self.data) == len(other.data):
            curr1, curr2 = self.data.header.next, other.data.header.next
            while curr1.data is not None and curr2.data is not None:
                if curr1.data == curr2.data:
                    curr1, curr2 = curr1.next, curr2.next
                else:
                    return False
            return True
        elif self < other:
            return True
        else:
            return False

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return other <= self
    
    def __repr__(self):
        curr = self.data.header.next
        s = ''
        while curr.next is not None:
            s += (curr.data[0] * curr.data[1])
            curr = curr.next
        return s
    
def main():
    s1 = CompactString('aaaaabbbaaac')
    s2 = CompactString('aaaaabbbaaac')
    s3 = s1 + s2
    print(s3)

#main()