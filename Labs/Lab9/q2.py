import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayDeque:
    INITIAL_CAPACITY = 8
    def __init__(self):
        self.data_arr = make_array(ArrayDeque.INITIAL_CAPACITY)
        self.capacity = ArrayDeque.INITIAL_CAPACITY
        self.n = 0
        self.front_ind = None

    def __len__(self):
        return self.n
    
    def is_empty(self):
        return len(self) == 0
    
    def first(self):
        if self.is_empty():
            raise Exception('empty')
        else:
            return self.data_arr[self.front_ind]
    
    def last(self):
         if self.is_empty():
            raise Exception('empty')
         else:
            return self.data_arr[(self.front_ind + len(self)) % self.capacity - 1]
    
    def enqueue_first(self, elem):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        if self.is_empty():
            self.data_arr[0] = elem
            self.front_ind = 0
            self.n += 1
        else:
            index = self.front_ind - 1
            self.data_arr[index] = elem
            self.front_ind = (self.front_ind - 1) % self.capacity
            self.n += 1
    
    def enqueue_last(self, elem):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        if (self.is_empty()):
            self.data_arr[0] = elem
            self.front_ind = 0
            self.n += 1
        else:
            back_ind = (self.front_ind + self.n) % self.capacity
            self.data_arr[back_ind] = elem
            self.n += 1

    def dequeue_first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % self.capacity
        self.n -= 1
        if(self.is_empty()):
            self.front_ind = None
        if((self.n < self.capacity // 4) and
                (self.capacity > ArrayDeque.INITIAL_CAPACITY)):
            self.resize(self.capacity // 2)
        return value
    
    def dequeue_last(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        back_ind = (self.front_ind+self.n) % self.capacity - 1
        value = self.data_arr[back_ind]
        self.data_arr[(self.front_ind+self.n) % self.capacity] = None
        self.n -= 1
        if self.is_empty():
            self.front_ind = None
        if((self.n < self.capacity // 4) and
                (self.capacity > ArrayDeque.INITIAL_CAPACITY)):
            self.resize(self.capacity // 2)
        return value


    def resize(self, new_cap):
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        for new_ind in range(self.n):
            new_data[new_ind] = self.data_arr[old_ind]
            old_ind = (old_ind + 1) % self.capacity
        self.data_arr = new_data
        self.capacity = new_cap
        self.front_ind = 0

def main():
    q = ArrayDeque()
    q.enqueue_last(2)
    q.enqueue_last(3)
    q.enqueue_last(4)
    q.enqueue_first(1)
    print(q.dequeue_last(), q.last())

main()