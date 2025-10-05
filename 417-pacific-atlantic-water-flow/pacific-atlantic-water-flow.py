class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
                return []

        m, n = len(heights), len(heights[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(i, j, visited):
            visited.add((i, j))
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    if (x, y) not in visited and heights[x][y] >= heights[i][j]:
                        dfs(x, y, visited)

        pa, at = set(), set()

        for j in range(n): 
            dfs(0, j, pa)

        for i in range(m): 
            dfs(i, 0, pa)

        for j in range(n): 
            dfs(m-1, j, at)

        for i in range(m): 
            dfs(i, n-1, at)

        return list(pa & at)