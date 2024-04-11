def permutations(lst, low, high):
    if low == high:
        return [[lst[low]]]
    else:
        temp = []
        for i in range(high - low + 1):
            for sub in permutations(lst, low + 1, high):
                sub.insert(i, lst[low])
                temp.append(sub)
        return temp

def main():
    lst = [1, 2 ,3]
    print(permutations(lst, 0 ,len(lst) - 1))

