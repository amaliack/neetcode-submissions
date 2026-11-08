class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        INF = 2 ** 31 - 1

        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: queue.append((i, j))
        
        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n: continue
                if grid[new_x][new_y] == -1: continue

                if grid[new_x][new_y] == INF:
                    grid[new_x][new_y] = grid[x][y] + 1
                    queue.append((new_x, new_y))


