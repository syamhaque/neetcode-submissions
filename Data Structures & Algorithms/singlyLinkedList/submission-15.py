class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        self.length = 0
    
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        curr = self.head.next
        i = index
        while i:
            curr = curr.next
            i -= 1

        return curr.val

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val, self.head)
        new_head.next = self.head.next
        self.head.next = new_head

        if not new_head.next:
            self.tail = new_head
        self.length += 1

    def insertTail(self, val: int) -> None:
        new_tail = ListNode(val)
        self.tail.next = new_tail
        self.tail = self.tail.next

        self.length += 1

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False        

        curr = self.head
        i = index
        while i:
            curr = curr.next
            i -= 1

        if index == self.length - 1:
            self.tail = curr
        curr.next = curr.next.next
        
        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        array = []
        curr = self.head.next
        for i in range(self.length):
            array.append(curr.val)
            curr = curr.next
        
        return array
