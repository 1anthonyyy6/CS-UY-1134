def split_by_sign(lst, low, high):
    if low < high:
        if lst[low] < 0:
            split_by_sign(lst, low + 1, high)
        elif lst[high] >= 0:
            split_by_sign(lst, low, high - 1)
        else:
            lst[low], lst[high] = lst[high], lst[low]
            split_by_sign(lst, low + 1, high - 1)

def main():
    lst = [1, -2, 3, -10, -13, -15, 12, 9, 0, 10]
    split_by_sign(lst, 0, len(lst) - 1)
    print(lst)

