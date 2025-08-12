class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
       MOD = 10**9 + 7
       dp = [[-1] * (n + 1) for _ in range(n + 1)]  
       
       def fun(st, val):
            if val == 0:
                return 1  
            if st > n:
                return 0  
            if dp[st][val] != -1:
                return dp[st][val]  

            ans = 0
            pwr = st ** x
            if pwr <= val:
                ans = (ans + fun(st + 1, val - pwr)) % MOD

            ans = (ans + fun(st + 1, val)) % MOD
            dp[st][val] = ans
 
            return ans

       return fun(1, n)