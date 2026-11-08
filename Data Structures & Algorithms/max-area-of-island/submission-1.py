class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        max_area = 0
        m = len(grid)
        n = len(grid[0])

        def bfs(x, y):
            area = 0
            queue = deque()

            queue.append((x, y))
            visited.add((x, y))
            while queue:
                x_prime, y_prime = queue.popleft()
                area += 1
                for dx, dy in directions:
                    new_x = x_prime + dx
                    new_y = y_prime + dy
                    
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n: 
                        continue
                    
                    if (new_x, new_y) not in visited and grid[new_x][new_y] == 1:
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    curr_area = bfs(i, j)
                    max_area = max(max_area, curr_area)
                visited.add((i, j))
        return max_area

