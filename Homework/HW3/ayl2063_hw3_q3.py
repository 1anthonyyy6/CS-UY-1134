#a 
def find_duplicates(lst):
    dupe = []
    n = len(lst)
    counter = [0 for i in range(n)]
    for i in range(n):
        counter[lst[i]] += 1
    for i in range(n):
        if counter[i] > 1:
            dupe.append(i)
    return dupe

def main():
    lst = [2,4,4,1,2]
    print(find_duplicates(lst))

#b
#O(n)