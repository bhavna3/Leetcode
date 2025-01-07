class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r: int, c: int)-> None:

            grid[r][c] = '0'
            for dr,dc in ((0,1),(1,0),(0,-1),(-1,0)):
                if grid[r+dr][c+dc] == '1':
                    dfs(r+dr,c+dc)

            return
        ans, rows, cols = 0, len(grid), len(grid[0])
        grid = [['0']*(cols+2)] + [['0']+x+['0'] for x in grid] + [['0']*(cols+2)]
        
        for r in range(1,rows+1):
            for c in range(1,cols+1):

                if grid[r][c] != '1': continue
                ans+= 1
                dfs(r,c) 
        return ans