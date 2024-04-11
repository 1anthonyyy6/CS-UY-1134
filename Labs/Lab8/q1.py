from Lab9.ArrayStack import ArrayStack

def stack_sum(s):
    if s.is_empty():
        return 0
    elif len(s) == 1:
        return s.top() 
    else:
        val = s.pop()
        sum = val + stack_sum(s)
        s.push(val)
        return sum

def main():
    lst = [1,-14,5,6,-7,9,10,-5,-8]
    s = ArrayStack()
    for i in range(len(lst)):
        s.push(lst[i])
    print(stack_sum(s))

main()