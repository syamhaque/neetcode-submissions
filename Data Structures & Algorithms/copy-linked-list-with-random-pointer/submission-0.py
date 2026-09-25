"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_copy_node_map = {None:None}

        dummy = head
        while dummy:
            copy = Node(dummy.val, None, None)
            original_to_copy_node_map[dummy] = copy
            dummy = dummy.next

        dummy = head
        while dummy:
            copy = original_to_copy_node_map[dummy]
            copy.next = original_to_copy_node_map[dummy.next]
            copy.random = original_to_copy_node_map[dummy.random]
            dummy = dummy.next
        
        return original_to_copy_node_map[head]
