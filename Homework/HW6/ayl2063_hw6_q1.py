from DoublyLinkedList import DoublyLinkedList

class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0
    
    def enqueue(self,val):
        self.data.add_last(val)

    def dequeue(self):
        if self.is_empty():
            raise Exception('empty')
        temp = self.data.delete_first()
        return temp

    def first(self):
        if self.is_empty():
            raise Exception('empty')
        return self.data.header.next.data