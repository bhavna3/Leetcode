class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        N=10000000
        dp=[[N for i in range(n)] for j in range(n)]
        for t in times:
            dp[t[0]-1][t[1]-1]=t[2]
        for i in range(n):dp[i][i]=0
        ans=0
        for l in range(n):
            for i in range(n):
                for j in range(n):
                    if(dp[i][j]>dp[i][l]+dp[l][j]):dp[i][j]=dp[i][l]+dp[l][j]
        for i in range(n):
            ans=max(dp[k-1][i],ans)
        if(ans>=N):return -1
        return ans     