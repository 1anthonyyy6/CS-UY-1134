from DoublyLinkedList import DoublyLinkedList

class MidStack():
    def __init__(self):
        self.data = DoublyLinkedList()
        self.mid = None

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self.data.add_last(e)
        if len(self) == 1:
            self.mid = self.data.header.next
        elif len(self) % 2 == 1:
            self.mid = self.mid.next 

    def top(self):
        if self.is_empty():
            raise Exception('empty')
        else:
            return self.data.trailer.prev.data

    def pop(self):
        if self.is_empty():
            raise Exception('empty')
        else:
            res = self.data.delete_last()
            if self.is_empty():
                self.mid = None
            elif len(self) % 2 == 1:
                self.mid = self.mid.prev
            return res

    def mid_push(self, e):
        self.data.add_after(self.mid, e)
        if len(self) % 2 == 1:
            self.mid = self.mid.next

def main():
    m = MidStack()
    for i in range(5):
        m.push(i)
    m.mid_push(10)
    for i in range(len(m)):
        print(m.pop())
    
main()