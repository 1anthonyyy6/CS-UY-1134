from ArrayStack import ArrayStack

class Queue:
    def __init__(self):
        self.inStack = ArrayStack()
        self.outStack = ArrayStack()

    def __len__(self):
        return len(self.inStack) + len(self.outStack)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, elem):
        self.inStack.push(elem)

    def dequeue(self):
        if self.is_empty():
            raise Exception('empty')
        if self.outStack.is_empty():
            while not self.inStack.is_empty():
                self.outStack.push(self.inStack.pop())
        return self.outStack.pop()

    def first(self):
        if self.is_empty():
            raise Exception('empty') 
        if self.outStack.is_empty():
            while not self.inStack.is_empty():
                self.outStack.push(self.inStack.pop())
        return self.outStack.top()

def main():
    q = Queue()
    for i in range(5):
        q.enqueue(i)
    print(len(q))
