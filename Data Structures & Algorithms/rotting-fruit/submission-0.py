class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        fresh = 0
        count = 0
    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: queue.append((i, j))
                if grid[i][j] == 1: fresh += 1
        
        while queue and fresh > 0:
            for i in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n: continue
                    if grid[new_x][new_y] == 0: continue

                    if grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        queue.append((new_x, new_y))
                        fresh -= 1
            count += 1
        
        return -1 if fresh > 0 else count
