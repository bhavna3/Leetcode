class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        maxx = max(nums) + k + 2
        count = [0] * maxx
        for v in nums:
            count[v] += 1

        for i in range(1, maxx):
            count[i] += count[i - 1]
        res = 0
        for i in range(maxx):
            l = max(0, i - k)
            r = min(maxx - 1, i + k)
            tot = count[r] - (count[l - 1] if l else 0)
            freq = count[i] - (count[i - 1] if i else 0)
            res = max(res, freq + min(numOperations, tot - freq))

        return res
        