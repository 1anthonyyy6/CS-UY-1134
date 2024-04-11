def intersectionOfLst(lst1, lst2):
    curr1, curr2 = 0,0
    n1, n2 = len(lst1), len(lst2)
    lst = []
    while curr1 < n1 and curr2 < n2:
        if lst1[curr1] < lst2[curr2]:
            curr1 += 1
        elif lst1[curr1] > lst2[curr2]:
            curr2 += 1
        else:
            lst.append(lst1[curr1])
            curr1 += 1
            curr2 += 1
    return lst

def main():
    lst1 = [1,2,3,4,5]
    lst2 = [2,3,4,5,6]
    print(intersectionOfLst(lst1, lst2))

main()