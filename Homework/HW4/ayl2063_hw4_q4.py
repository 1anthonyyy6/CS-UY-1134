def list_min(lst, low, high):
    if high == low:
        return lst[low]
    else:
        if lst[low] < lst[high]:
            return list_min(lst, low, high - 1)
        else:
            return list_min(lst, low + 1,high)

def main():
    lst = [3, 4, 2, 103, 5, 10, 12, 13]
    print(list_min(lst, 0, len(lst) - 1))

