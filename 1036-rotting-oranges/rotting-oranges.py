class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = list() # queue
        count = -1

        # Get all rotten oranges
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append([i,j])


        while q:

            tmp = q.copy()
            q.clear()

            for i,j in tmp:

                if i+1 < ROWS and grid[i+1][j] == 1:
                    q.append([i+1, j])
                    grid[i+1][j] = 2

                if j+1 < COLS and grid[i][j+1] == 1:
                    q.append([i, j+1])
                    grid[i][j+1] = 2

                if i-1 >= 0 and grid[i-1][j] == 1:
                    q.append([i-1, j])
                    grid[i-1][j] = 2

                if j-1 >= 0 and grid[i][j-1] == 1:
                    q.append([i, j-1])
                    grid[i][j-1] = 2

            count += 1
        

        for row in grid:
            for col in row:
                if col == 1:
                    return -1
            

        return count if count >= 0 else 0