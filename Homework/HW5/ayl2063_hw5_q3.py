from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack:
    def __init__(self):
        self.data_bottom = ArrayStack()
        self.data_top = ArrayDeque()

    def __len__(self):
        return len(self.data_bottom) + len(self.data_top)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        if self.is_empty():
            self.data_bottom.push(e)
        else:
            self.data_top.enqueue_last(e)
            if len(self) % 2 == 1:
                temp = self.data_top.dequeue_first()
                self.data_bottom.push(temp)

    def top(self):
        if self.is_empty():
            raise Exception('empty')
        if len(self) == 1:
            val = self.data_bottom.top()
        else:
            val = self.data_top.last()
        return val

    def pop(self):
        if self.is_empty():
            raise Exception('empty')
        if len(self) == 1:
            val = self.data_bottom.pop()
        else:
            val = self.data_top.dequeue_last()
            if len(self) % 2 == 0:
                temp = self.data_bottom.pop()
                self.data_top.enqueue_first(temp)
        return val

    def mid_push(self, e):
        if len(self) % 2 == 1:
            self.data_top.enqueue_first(e)
        else:
            self.data_bottom.push(e)
        
def main():
    midS = MidStack()
    midS.push(2)
    midS.push(4)
    midS.push(6)
    midS.push(8)
    midS.mid_push(10)
    mid = MidStack()
    mid.push(2)
    mid.push(4)
    mid.push(6)
    mid.push(8)
    mid.push(10)
    mid.mid_push(12)
    for i in range(len(midS)):
        print(midS.pop())
    print('\n')
    for i in range(len(mid)):
        print(mid.pop())
#main()    