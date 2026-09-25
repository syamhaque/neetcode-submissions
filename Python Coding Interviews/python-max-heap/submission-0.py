import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = []
    for num in nums:
        max_heap.append(-num)
    heapq.heapify(max_heap)

    max_heap.sort()
    for i in range(len(max_heap)):
        max_heap[i] = -max_heap[i]

    return max_heap

# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
