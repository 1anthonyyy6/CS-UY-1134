def fibs(n):
    a, b = 0, 1
    yield b
    while n > 1:
        a, b, n = b, a + b, n - 1
        yield b

def main():
    for curr in fibs(8):
        print(curr)

