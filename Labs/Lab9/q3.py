from ArrayQueue import ArrayQueue

def flatten_list_by_depth(lst):
    q = ArrayQueue()
    new_lst = []
    for i in range(len(lst)):
        q.enqueue(lst[i])
    while not q.is_empty():
        temp = q.dequeue()
        if type(temp) is not list:
            new_lst.append(temp)
        else:
            for i in temp:
                q.enqueue(i)
    return new_lst

def main():
    lst = [[[[0]]],[1,2],3,[4,[5,6,[7]],8],9]
    new_lst = flatten_list_by_depth(lst)
    print(flatten_list_by_depth(lst))

main()