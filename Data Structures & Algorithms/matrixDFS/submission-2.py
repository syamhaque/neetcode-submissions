class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(grid, r, c, visit):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 1 or (r, c) in visit:
                return 0
            
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            visit.add((r, c))
            count = 0
            for dir in dirs:
                dr, dc = dir[0], dir[1]
                count += dfs(grid, r + dr, c + dc, visit)
            
            visit.remove((r, c))
            return count

        return dfs(grid, 0, 0, visit)