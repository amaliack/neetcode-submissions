class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        res = []
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def bfs(queue, visited):
            while queue:
                x, y = queue.popleft()
                visited.add((x, y))
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy

                    # boundary check
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n: continue

                    if heights[new_x][new_y] >= heights[x][y] and (new_x, new_y) not in visited:
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))

        # pacific stuff
        pac_visited = set()
        pac_queue = deque()
        for i in range(m):
            pac_queue.append((i, 0))
        for j in range(n):
            pac_queue.append((0, j))

        # atlantic stuff
        atl_visited = set()
        atl_queue = deque()
        for i in range(m):
            atl_queue.append((i, n - 1))
        for j in range(n):
            atl_queue.append((m - 1, j))

        bfs(pac_queue, pac_visited)
        bfs(atl_queue, atl_visited)
        for x,y in pac_visited:
            if (x, y) in atl_visited: res.append([x, y])
        return res



        
