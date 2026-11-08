class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # we do a bfs from different starting points
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        islands = 0
        m = len(grid)
        n = len(grid[0])

        def bfs(x, y):
            queue = deque()
            queue.append((x, y))
            while queue:
                x_prime, y_prime = queue.popleft()
                for dx, dy in directions:
                    new_x = x_prime + dx
                    new_y = y_prime + dy
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n: continue
                    if (new_x, new_y) not in visited and grid[new_x][new_y] == '1':
                        queue.append((new_x, new_y))
                    visited.add((new_x, new_y))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    # we run the bfs again
                    bfs(i, j)
                    islands += 1
                visited.add((i, j))
        return islands

