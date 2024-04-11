from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue
from copy import copy

def permutations(lst):
    elements = ArrayStack()
    perm = ArrayQueue()
    while len(lst) > 0:
        temp = lst.pop()
        elements.push(temp)
    while not elements.is_empty():
        if perm.is_empty():
            perm.enqueue([elements.pop()])
        else:
            new_elem = elements.pop()
            for i in range(len(perm)):
                temp = perm.dequeue()
                for j in range(len(temp) + 1):
                    new_perm = copy(temp)
                    new_perm.insert(j, new_elem)
                    perm.enqueue(new_perm)
    perm_lst = []
    while not perm.is_empty():
        perm_lst.append(perm.dequeue())
    return perm_lst

def main():
    lst = [1,2,3]
    print(permutations(lst))

#main()            
