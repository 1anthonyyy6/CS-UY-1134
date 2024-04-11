from ArrayStack import ArrayStack

def postfix_calculator():
    var = {}
    def calculator(lst):
        s = ArrayStack()
        while len(lst) > 0:
            token = lst.pop()
            if token in '*-+/':
                val2 = s.pop()
                val1 = s.pop()
                if val1 in var:
                    val1 = var[val1]
                else:
                    val1 = int(val1)

                if val2 in var:
                    val2 = var[val2]
                else:
                    val2 = int(val2)

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
        return s.pop()
    
    finish = False
    while not finish:
        in_str = input('--> ')
        if in_str == 'done()':
            finish = True
        else:
            in_lst = in_str.split()
            if len(in_lst) == 1:
                if in_lst[0] in var:
                    print(var[in_lst[0]])
                else:
                    print(int(in_lst[0]))
            elif in_lst[1] == '=':
                var_name = in_lst[0]
                in_lst = in_lst[2:]
                var[var_name] = calculator(in_lst[::-1])
                print(var_name)
            else:
                print(calculator(in_lst[::-1]))

def main():
    postfix_calculator()

main()