from Lab9.q1 import reverse

def shift(lst, k):
    reverse(lst)
    for i in range(k):
        lst.append(lst[0])
        lst.remove(lst[0])
    reverse(lst)

def main():
    lst = [1,2,3,4,5,6]
    k = 2
    shift(lst, k)
    print(lst)

main()
