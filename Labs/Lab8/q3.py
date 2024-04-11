from Lab9.ArrayStack import ArrayStack

def flatten_list(lst):
    s = ArrayStack()
    while len(lst) > 0:
        s.push(lst.pop())
    while not s.is_empty():
        temp = s.pop()
        if type(temp) is not list:
            lst.append(temp)
        else:
            for i in range(len(temp) - 1, -1, -1):
                s.push(temp[i])

def main():
    lst =  [ [[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
    flatten_list(lst)
    print(lst)

main()
