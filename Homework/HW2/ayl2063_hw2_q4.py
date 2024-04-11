def e_approx(n):
    e = 1.0
    temp = 1.0
    for i in range(1, n + 1):
        temp /= i
        e += temp
    return e

def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)

