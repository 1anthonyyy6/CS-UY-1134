def flat_list(nested_lst, low, high):
    if low == high:
        if isinstance(nested_lst[low], int):
            return [nested_lst[low]]
        return flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1)
    else:
        return flat_list(nested_lst, low, low) + flat_list(nested_lst, low + 1, high)

def main():
    lst = [[1,2], 3, [4, [5,6,[7], 8]]]
    print(flat_list(lst, 0, len(lst) - 1))

