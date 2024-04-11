from random import randint

def create_permutation(n):
    lst = []
    for i in range(n):
        lst.append(i)
    for i in range(len(lst)):
        temp = lst.pop(i)
        lst.insert(randint(0, n-1), temp)
    return lst

print(create_permutation(6))

def scramble_word(word):
    l = len(word)
    perm = create_permutation(l)
    scrambled = ''
    for i in perm:
        scrambled += word[i]
    return scrambled

def guessingGame(word):
    print('Unscramble the word: ' + scramble_word(word))
    for i in range(3):
        t = input('Try #' + str(i + 1) + ': ')
        if t == word:
            print('Yay, you got it!')
            break
        else:
            print('Wrong!')

def main():
    guessingGame('pokemon')

main()