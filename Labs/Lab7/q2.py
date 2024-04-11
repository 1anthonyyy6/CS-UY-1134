def isPowerOfTwo(n):
    if n <= 1:
        return n == 1
    else:
        return isPowerOfTwo(n / 2)

def main():
    lst = [i for i in range(1000)]
    for i in lst:
        if isPowerOfTwo(i):
            print(i)

main()