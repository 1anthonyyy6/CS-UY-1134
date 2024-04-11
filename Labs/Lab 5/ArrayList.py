import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self, iter_collection = None):
        self.data_arr = make_array(1)
        self.capacity = 1
        self.n = 0
        if not iter_collection == None:
            for i in iter_collection:
                self.append(i)

    def __len__(self):
        return self.n

    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size


    def __getitem__(self, ind):
        if ind < 0:
            ind += self.n
        if (not (ind <= self.n - 1)):
            raise IndexError('invalid index')
        return self.data_arr[ind]


    def __setitem__(self, ind, val):
        if ind < 0:
            ind += self.n
        if (not (ind <= self.n - 1)):
            raise IndexError('invalid index')
        self.data_arr[ind] = val


    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  #could also yield self[i]


    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __add__(self, other):
        temp = ArrayList()
        for i in range(self.n):
            temp.append(self.data_arr[i])
        for i in range(other.n):
            temp.append(other.data_arr[i])
        return temp
    
    def __iadd__(self, other):
        for elem in other:
            self.append(elem)
        return self
    
    def __mul__(self, k):
        temp = ArrayList()
        for i in range(k):
            for i in range(self.n):
                temp.append(self.data_arr[i])
        return temp

    def __rmul__(self, k):
        return self * k
    
    def remove(self, n):
        i = 0
        while self.data_arr[i] != n:
            i += 1
        for i in range(i, self.n - 1):
            self.data_arr[i] = self.data_arr[i+1]
        self.data_arr[self.n - 1] = None
        self.n -= 1
    
    def removeAll(self, n):
        count = 0
        for i in range(self.n):
            if self.data_arr[i] == n:
                count += 1
        for i in range(count):
            self.remove(n)

    def __repr__(self):
        return '[' + ', '.join(str(self.data_arr[i]) for i in range(self.n)) + ']'

def main():
    arr = ArrayList()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    arr2 = ArrayList()
    arr2.append(4)
    arr2.append(5)
    arr2.append(6)
    arr3 = arr + arr2
    arr += arr2
    arr4 = 2 * arr
    print(arr[-1])
    print(arr4)
    arr5 = ArrayList(range(10))
    print(arr5)
    arr5.removeAll(2)
    print(arr5)

main()