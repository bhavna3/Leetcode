class Solution:
    def soupServings(self, n: int) -> float:
        threshold = 5000
        if n > threshold:
            return 1.0
        
        cache = {}
        
        def dfs(a=n, b=n):
            if (a, b) in cache:
                return cache[(a, b)]
            
            if a <= 0 and b <= 0:
                result = 0.5
            elif a <= 0:
                result = 1.0
            elif b <= 0:
                result = 0.0
            else:
                result = 0.25 * (dfs(a - 100, b) +
                               dfs(a - 75, b - 25) +
                               dfs(a - 50, b - 50) +
                               dfs(a - 25, b - 75))
            
            cache[(a, b)] = result
            return result
        
        return dfs()   