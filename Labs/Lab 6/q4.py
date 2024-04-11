def is_palindrome(str, low, high):
    if high - low <= 1:
        if str[low] == str[high]:
            return True
        else:
            return False
    else:
        if str[low] == str[high]:
            return is_palindrome(str, low + 1, high - 1)
        else:
            return False
        
def main():
    word = 'raceecar'
    print(is_palindrome(word, 0, 7))

main()