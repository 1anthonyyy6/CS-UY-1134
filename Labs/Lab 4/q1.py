def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

def main():
    s = '1racecar1'
    print(is_palindrome(s))

main()