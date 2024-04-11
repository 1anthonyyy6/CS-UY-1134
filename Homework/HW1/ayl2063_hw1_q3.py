#a
def sum_squares(n):
    sum = 0
    for i in range(n):
        sum += i * i
    return sum

#c
def odd_sum_squares(n):
    sum = 0
    for i in range(n):
        if i % 2 == 1:
            sum += i * i
    return sum

def main():
    n = 40
    #b
    s = [i * i for i in range(n)]
    s = sum(s)
    print(sum_squares(40), s)
    #d
    oddS = [i * i for i in range(n) if i % 2 == 1]
    oddS = sum(oddS)
    print(odd_sum_squares(n), oddS)

