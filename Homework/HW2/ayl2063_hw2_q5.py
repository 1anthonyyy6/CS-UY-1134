def split_parity(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst.append(lst.pop(i))

def main():
    lst = [1,2,3,4,5,6,7,8,9]
    split_parity(lst)
    print(lst)