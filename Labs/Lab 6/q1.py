def sum_to(n):
    if n == 0:
        return n
    else:
        return n + sum_to(n-1)

def main():
    print(sum_to(2))

main()