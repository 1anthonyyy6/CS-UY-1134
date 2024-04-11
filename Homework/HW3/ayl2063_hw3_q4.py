#a
#O(n^2)

#b
def remove_all(lst, value):
    shift = 0
    for i in range(len(lst)):
        if lst[i] == value:
            shift += 1
        else:
            lst[i - shift] = lst[i]
    for i in range(shift):
        lst.pop()

def main():
    lst = [1,3,2,3,3,4,3,6,3,7,1,2,3]
    print(lst)
    remove_all(lst, 3)
    print(lst)


#c O(n)