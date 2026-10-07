class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1
            
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        queue = deque()
        visit = set()

        queue.append((0, 0))
        visit.add((0, 0))

        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                for dr, dc in dirs:
                    new_r, new_c = r + dr, c + dc
                    if min(new_r, new_c) < 0 or new_r >= ROWS or new_c >= COLS or grid[new_r][new_c] == 1 or (new_r, new_c) in visit:
                        continue

                    queue.append((new_r, new_c))
                    visit.add((new_r, new_c))

            length += 1
        
        return -1