class SinglyLinkedList:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next
        
        def disconnect(self):
            self.data = None
            self.next = None

    def __init__(self):
        self.header = None
        self.tail = None
        self.n = 0

    def __len__(self):
        return self.n
    
    def is_empty(self):
        return len(self) == 0
    
    def add_after(self, node, val):
        new_node = SinglyLinkedList.Node(val)
        if node.next is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            next_node = node.next
            node.next = new_node
            new_node.next = next_node
        self.n += 1
    
    def add_first(self, val):
        new_node = SinglyLinkedList.Node(val)
        if self.is_empty():
            self.header = new_node
            self.tail = new_node
        else:
            new_node.next = self.header
            self.header = new_node
        self.n += 1
    
    def add_last(self, val):
        if self.is_empty():
            new_node = SinglyLinkedList.Node(val)
            self.header = new_node
            self.tail = new_node
            self.n += 1
        else:
            self.add_after(self.tail, val)

    def delete_first(self):
        if self.is_empty():
            raise Exception('empty')
        elif len(self) == 1:
            temp = self.header
            self.header = None
            self.tail = None
            self.n -= 1
            return temp
        else:
            temp = self.header
            self.header = self.header.next
            temp.disconnect()
            self.n -= 1
            return temp
    
    def delete_last(self):
        if self.is_empty():
            raise Exception('empty')
        elif len(self) == 1:
            i = self.header
            self.header = None
            self.tail = None
            self.n -= 1
            return i
        else:
            i = self.tail
            curr = self.header
            for i in range(len(self)-2):
                curr = curr.next
            self.tail.disconnect()
            self.tail = curr
            curr.next = None
            self.n -= 1
            return i
    
    def reverse(self):
        if len(self) <= 1:
            return
        else:
            for i in range(len(self)):
                temp = self.delete_first()
                self.add_last(temp)
    
    def __iter__(self):
        cursor = self.header.next
        while(cursor is not None):
            yield cursor.data
            cursor = cursor.next
            
    def __repr__(self):
        return "[" + " -> ".join([str(elem) for elem in self]) + "]"

def main():
    a = SinglyLinkedList()
    for i in range(10):
        a.add_first(i)
    a.delete_last()
    print(a)

main()
    

        
