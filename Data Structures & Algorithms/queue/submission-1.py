class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0


    def isEmpty(self) -> bool:
        return self.length == 0

    def append(self, value: int) -> None:
        new_tail = Node(value)
        curr_tail = self.tail.prev

        curr_tail.next = new_tail
        new_tail.next = self.tail
        new_tail.prev = curr_tail
        self.tail.prev = new_tail

        self.length += 1

    def appendleft(self, value: int) -> None:
        new_head = Node(value)
        curr_head = self.head.next

        curr_head.prev = new_head
        new_head.prev = self.head
        new_head.next = curr_head
        self.head.next = new_head
        
        self.length += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        val = self.tail.prev.value
        new_tail = self.tail.prev.prev
        new_tail.next = self.tail
        self.tail.prev = new_tail

        self.length -= 1
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        val = self.head.next.value
        new_head = self.head.next.next
        self.head.next = new_head
        new_head.prev = self.head

        self.length -= 1
        return val
        
