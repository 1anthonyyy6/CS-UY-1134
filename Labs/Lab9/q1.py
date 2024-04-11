from ArrayStack import ArrayStack

def eval_prefix(exp_str):
    exp_lst = exp_str.split()[::-1]
    s = ArrayStack()
    for token in exp_lst:
        if token in '*-+/':
            val1 = int(s.pop())
            val2 = int(s.pop())
            if token == '*':
                res = val1 * val2
            elif token == '-':
                res = val1 - val2
            elif token == '+':
                res = val1 + val2
            else:
                if val2 == 0:
                    raise ZeroDivisionError
                res = val1 / val2
            s.push(res)
        else:
            s.push(token)
    return s.top()

def main():
    exp_str = '- + * 16 5 * 8 4 20'
    print(eval_prefix(exp_str))

main()
