def count_lowercase(s, low, high):
    if low == high:
        if s[low].islower():
            return 1
        else:
            return 0
    else:
        count = 0
        if s[low].islower():
            count += 1
        count += count_lowercase(s, low + 1, high)
        return count

def is_number_of_lowercase_even(s, low, high):
    if low == high:
        return not s[low].islower()
    else:
        return not is_number_of_lowercase_even(s, low, low) ^ is_number_of_lowercase_even(s, low + 1, high)
    
def main():
    s = 'asdAPSODIJASdhs'
    print(count_lowercase(s, 0, len(s) - 1), is_number_of_lowercase_even(s, 0, len(s) - 1))

