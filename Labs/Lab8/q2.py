from Lab9.ArrayStack import ArrayStack

class MeanStack:
    def __init__(self):
        self.data = ArrayStack()
        self.s = 0
    
    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self) == 0
    
    def push(self, e):
        if type(e) is not float and type(e) is not int:
            raise TypeError
        else:
            self.data.push(e)
            self.s += e
    
    def pop(self):
        temp = self.data.pop()
        self.s -= temp
        return temp
    
    def top(self):
        return self.data.top()
    
    def sum(self):
        return self.s
    
    def mean(self):
        return self.s / len(self)

def main():
    s = MeanStack()
    lst = [1.0,2.0,3.0,4.0,5.0,6.0,7,8]
    for i in lst:
        s.push(i)
    print(s.sum())
    print(s.mean())

main()