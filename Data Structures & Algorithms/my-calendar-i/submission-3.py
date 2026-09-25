from sortedcontainers import SortedSet
class MyCalendar:
    
    def __init__(self):
        self.events = SortedSet()

    def book(self, startTime: int, endTime: int) -> bool:
        event = (startTime, endTime)
        i = self.events.bisect_left(event)
        if i > 0 and self.events[i-1][1] > event[0]:
            return False
        if i < len(self.events) and self.events[i][0] < event[1]:
            return False
        
        self.events.add(event)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)