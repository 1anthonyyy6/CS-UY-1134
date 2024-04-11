def reverse(n, low = None, high = None):
    if low == None and high == None:
        i, j = 0, len(n) - 1
    else:
        i, j = low, high
    while i < j:
        a, b = n[i], n[j]
        n[i], n[j] = b, a
        i += 1
        j -= 1

def main():
    n = [1,2,3,4,5,6]
    reverse(n,1,3)
    print(n)

main()
