class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        visited = set()

        # Add all treasure cells
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
                    visited.add((i, j))

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while q:
            r, c, dist = q.popleft()

            for dr, dc in directions:
                x = r + dr
                y = c + dc

                if (
                    x < 0 or x >= m or
                    y < 0 or y >= n or
                    grid[x][y] == -1 or
                    (x, y) in visited
                ):
                    continue

                # Update this room with its shortest distance
                grid[x][y] = dist + 1

                visited.add((x, y))
                q.append((x, y, dist + 1))