"""
a) Θ(n^2)
"""
#b
def find_missing(lst):
    low = 0
    high = len(lst) - 1
    while low < high:
        mid = (low + high) // 2
        if lst[mid] == mid:
            low = mid + 1
        else:
            high = mid - 1
    return low

#c
def find_missing_unsorted(lst):
    max = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max:
            max = lst[i]
    return sum(range(max + 1)) - sum(lst)

def main():
    lst = [0,1,2,3,4,5,7,8]
    lst1 = [8,6,0,4,3,5,1,2]
    print(find_missing(lst))
    print(find_missing_unsorted(lst1))
    
main()