from ArrayStack import ArrayStack

class MaxStack():
    def __init__(self):
        self.data = ArrayStack()
        self.maximum = None
    
    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.push((e, self.maximum))
        if self.maximum is None or e > self.maximum:
            self.maximum = e

    def pop(self):
        if self.is_empty():
            raise Exception('empty')
        temp = self.data.pop()
        val = temp[0]
        if temp[1] is None or temp[0] > temp[1]:
            self.maximum = temp[1]
        return val
    
    def top(self):
        if self.is_empty():
            raise Exception('empty')

        return self.data.top()[0]
    def max(self):
        if self.is_empty():
            raise Exception('empty')
        return self.maximum

def main():
    maxS = MaxStack()
    maxS.push(3)
    maxS.push(1)
    maxS.push(6)
    maxS.push(4)
    print(maxS.max())
    print(maxS.pop())
    print(maxS.pop())
    print(maxS.max())

#main()