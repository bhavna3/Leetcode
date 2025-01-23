class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]
        
        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]

        def validCell(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        self.size = 0
        def dfs(r, c):
            visited[r][c] = True

            for dr, dc in directions:
                nR, nC = r + dr, c + dc
                if validCell(nR, nC) and not visited[nR][nC] and grid[nR][nC] == 1:
                    self.size += 1
                    dfs(nR, nC)
                    
        maxIsland = 0
        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c] == 1:
                    dfs(r, c)
                    maxIsland = max(maxIsland, self.size+1)
                    self.size = 0
        
        return maxIsland   