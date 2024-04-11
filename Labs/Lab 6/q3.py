#a: n^2
#b
def find_max(lst, low, high):
    if high == low:
        return lst[low]
    else:
        if (lst[low] > lst[high]):
            return find_max(lst, low, high - 1)
        else:
            return find_max(lst, low + 1, high)

def main():
    lst = [13,9,16,16,3,4,2]
    print(find_max(lst, 0, 6))

main()