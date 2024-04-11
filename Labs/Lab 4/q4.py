def find_pivot(lst):
    low = 0
    high = len(lst) - 1
    while low < high:
        mid = (low + high) // 2
        if lst[mid] > lst[mid + 1]:
            return mid + 1
        elif lst[mid] < lst[high]:
            high = mid
        else:
            low = mid
    return None

def shift_binary_search(lst, target):
    piv = find_pivot(lst)
    if target <= lst[piv - 1] and lst[0] <= target:
        low = 0
        high = piv 
    else:
        low = piv
        high = len(lst) - 1
    while low < high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif target < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None

def main():
    lst = [15, 20, 21, 1, 3, 6, 7 ,10, 12, 14]
    target = 3
    print(find_pivot(lst))
    print(shift_binary_search(lst, target))
main()