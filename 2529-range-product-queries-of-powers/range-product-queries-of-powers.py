class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 1000000007
        powers = []
        answers = [0] * len(queries)
        i = 1
        product = 1

        while i <= n:
            i *= 2

        while n > 0:
            if n >= i:
                n -= i
                powers.append(i)
            i //= 2

        powers.sort()

        for i in range(len(queries)):
            product = 1
            l, r = queries[i]
            while l <= r:
                product = (product * powers[l]) % MOD
                l += 1
            answers[i] = product

        return answers