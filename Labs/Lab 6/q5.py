def binary_search(lst, low, high, val):
    if high - low <=1:
        if lst[low] != val:
            return None
        else:
            return lst[low]
    else:
        mid = (high + low) // 2
        print(low, mid, high)
        if val == lst[mid]:
            return mid
        elif val < lst[mid]:
            return binary_search(lst, low, mid - 1, val)
        else:
            return binary_search(lst, mid + 1, high, val)

def main():
    lst = [1,2,3,5,16,18,120, 140]
    print(binary_search(lst, 0, len(lst) - 1, 6))

main()