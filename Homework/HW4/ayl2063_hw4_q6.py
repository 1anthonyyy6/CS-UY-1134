def appearances(s, low, high):
    if low == high:
        return {s[low]: 1}
    else:
        temp = appearances(s, low + 1, high)
        if s[low] in temp:
            temp[s[low]] += 1
        else:
            temp[s[low]] = 1
        return temp

def main():
    s = 'Hello    World'
    print(appearances(s, 0, 10))


