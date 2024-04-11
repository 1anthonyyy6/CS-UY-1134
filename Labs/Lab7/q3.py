def split_parity(lst, low, high):
    if low < high:
        if lst[low] % 2 != 0 and lst[high] % 2 == 0:
            lst[low], lst[high] = lst[high], lst[low]
            split_parity(lst, low + 1, high - 1)
        elif lst[low] % 2 == 0 and lst[high] % 2 != 0:
            split_parity(lst, low + 1, high - 1)
        elif lst[low] % 2 != 0 and lst[high] % 2 != 0:
            split_parity(lst, low, high - 1)
        else:
            split_parity(lst, low + 1, high)

def main():
    lst = [4,-5,2,3,-1,-6,7,9,0]
    split_parity(lst, 0, len(lst) - 1)
    print(lst)

main()