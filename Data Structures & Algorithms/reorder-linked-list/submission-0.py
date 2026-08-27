# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = l2 = head

        while l2.next and l2.next.next:
            l1 = l1.next
            l2 = l2.next.next
        
        curr = l1.next
        prev = l1.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        l3 = head
        while prev:
            temp1, temp2 = l3.next, prev.next
            l3.next = prev
            prev.next = temp1
            l3, prev = temp1, temp2
