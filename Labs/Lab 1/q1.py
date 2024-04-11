def can_construct(word, letters):
    for i in word:
        if i not in letters:
            return False
        else:
            letters = letters[:letters.index(i)] + letters[letters.index(i) + 1: len(letters)]
    return True

def main():
    print(can_construct('apples', 'aplespl'))
    print(can_construct('apples', 'aples'))

main()