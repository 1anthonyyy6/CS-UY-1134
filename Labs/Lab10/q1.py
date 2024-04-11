from DoublyLinkedList import DoublyLinkedList

class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0
    
    def push(self, e):
        self.data.add_last(e)

    def top(self):
        if self.is_empty():
            raise Exception('empty')
        else:
            return self.data.trailer.prev.data

    def pop(self):
        if self.is_empty():
            raise Exception('empty')
        else:
            return self.data.delete_last()

def main():
    x = LinkedStack()
    x.push(1)
    x.push(2)
    x.push(3)
    x.push(4)
    for i in range(3):
        print(x.pop())
    print(x.top())

main()