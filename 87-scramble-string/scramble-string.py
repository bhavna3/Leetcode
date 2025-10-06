class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}

        def helper(x, y):
            if (x, y) in memo:
                return memo[(x, y)]

            if x == y:
                memo[(x, y)] = True
                return True

            if sorted(x) != sorted(y): 
                memo[(x, y)] = False
                return False

            n = len(x)
            for i in range(1, n):
                # no swap
                if helper(x[:i], y[:i]) and helper(x[i:], y[i:]):
                    memo[(x, y)] = True
                    return True

                # swap
                if helper(x[:i], y[-i:]) and helper(x[i:], y[:-i]):
                    memo[(x, y)] = True
                    return True

            memo[(x, y)] = False
            return False

        return helper(s1, s2)






            

        
        