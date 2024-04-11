def findChange(lst01):
    left = 0
    right = len(lst01) - 1
    mid = right // 2
    if lst01[left] == 0 and lst01[left + 1] == 1:
        return left + 1
    elif lst01[right - 1] == 0 and lst01[right] == 1:
        return right
    while left < right - 1:
        if lst01[mid - 1] == 0 and lst01[mid] == 1:
            return mid
        elif lst01[mid - 1] == 0 and lst01[mid] == 0:
            left = mid
            mid = (left + right) // 2
        else:
            right = mid
            mid = (left + right) // 2
    return "None"

def main():
    lst01 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    print(findChange(lst01))