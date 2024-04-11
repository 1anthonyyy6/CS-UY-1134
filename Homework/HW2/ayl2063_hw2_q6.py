def two_sum(srt_lst, target):
    left = 0
    right = len(srt_lst) - 1
    while left < right:
        if srt_lst[left] + srt_lst[right] == target:
            return (left, right)
        elif srt_lst[left] + srt_lst[right] < target:
            left += 1
        else:
            right -= 1
    return None

def main():
    lst = [-2,7,11,15,20,21]
    print(two_sum(lst, 22))
