from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    res = [i for i in arr[::-1]]
    return res


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
