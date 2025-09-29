class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        if n < 3:
            return 0

        dp = [[0] * n for _ in range(n)]
        
        for l in range(3, n + 1):
            for i in range(0, n - l + 1):
                j = i + l - 1
                res = float('inf')
                
                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    if cost < res:
                        res = cost
                dp[i][j] = res

        return dp[0][n-1]