def factors(num):
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            yield i
    for i in range(int(num**0.5) - 1, 0, -1):
        if num % i == 0:
            yield num // i

def main():
    for curr in factors(100):
        print(curr)

