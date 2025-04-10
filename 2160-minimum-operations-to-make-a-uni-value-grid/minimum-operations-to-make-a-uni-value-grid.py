class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        rem = grid[0][0] % x
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                arr.append(grid[i][j])
                if grid[i][j] % x != rem: return -1

        arr.sort()
        med = arr[len(arr)//2]
        res = 0
        for i in range(0, len(arr)):
            res += abs(arr[i] - med) / x
        return int(res)