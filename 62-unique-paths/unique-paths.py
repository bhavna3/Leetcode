class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0] * n for _ in range(m)]

        arr[m - 1] = [1] * n

        for i in range(m):
            arr[i][n - 1] = 1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                arr[i][j] = arr[i + 1][j] + arr[i][j + 1]

        return arr[0][0]