def reverse_vowels(input_str):
    vowels = 'aeiou'
    lst = list(input_str)
    low = 0
    high = len(lst) - 1
    while low < high:
        if lst[low] in vowels and lst[high] in vowels:
            lst[low], lst[high] = lst[high], lst[low]
            low += 1
            high -= 1
        if lst[low] not in vowels:
            low += 1
        if lst[high] not in vowels:
            high -= 1
    return "".join(lst)

def main():
    s = 'computer'
    print(reverse_vowels(s))

main()