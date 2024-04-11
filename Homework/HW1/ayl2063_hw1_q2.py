def shift(lst, k, shift = 'left'):
    if shift == 'left':
        for i in range(k):
            lst.append(lst.pop(0))
    else:
        for i in range(k):
            lst.insert(0, lst.pop(len(lst) - 1))

def main():
    lst = [1, 2, 3, 4, 5, 6]
    shift(lst, 4, 'right')
    print(lst)

