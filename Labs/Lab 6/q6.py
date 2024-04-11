def vc_count(word, low, high):
    if low == high:
        if word[low] in 'aeiouAEIOU':
            return (1,0)
        else:
            return (0,1)
    else:
        if word[low] in 'aeiouAEIOU':
            temp = vc_count(word, low + 1, high)
            return (1 + temp[0], temp[1])
        else:
            temp = vc_count(word, low + 1, high)
            return (temp[0], 1 + temp[1])

def main():
    word = 'NYUTandonEngineering'
    print(vc_count(word, 0, len(word) - 1))

main()