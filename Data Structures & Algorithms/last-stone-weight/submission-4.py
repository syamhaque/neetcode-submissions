class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x == y:
                continue
            elif x < y:
                y -= x
                heapq.heappush(stones, -y)
            else:
                x -= y
                heapq.heappush(stones, -x)
        
        return 0 if not stones else -stones[0]