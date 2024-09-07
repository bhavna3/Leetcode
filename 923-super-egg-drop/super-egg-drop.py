class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        D1 = [0] * (k + 1)
        for d in range(1, n + 1):
            D0 = D1
            D1 = [0] * (k + 1)
            for i in range(1, k + 1):
                D1[i] = D0[i] + D0[i - 1] + 1
            if D1[-1] >= n:
                return d
        return -1       