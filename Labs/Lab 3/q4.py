def maxSum(nums, k):
    s = 0
    for i in range(k):
        s += nums[i]
    i, j = 0, k
    maxS = s
    while j < len(nums):
        s += nums[j] - nums[i]
        if s > maxS:
            maxS = s
        i += 1
        j += 1
    return maxS


def main():
    nums = [1, 12, -5, -6, 50, 3]
    k = 3
    print(maxSum(nums, k))

main()
