def move_zeros(nums):
    i, j = 0, 0
    while i < len(nums):
        if nums[i - j] == 0:
            temp = nums[i - j]
            nums.remove(temp)
            nums.append(temp)
            j += 1
        i += 1

def main():
    nums = [0, 1, 0, 3, 13, 0]
    move_zeros(nums)
    print(nums)

main()