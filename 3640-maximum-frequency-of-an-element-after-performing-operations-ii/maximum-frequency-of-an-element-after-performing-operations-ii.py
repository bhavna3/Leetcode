class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        if n == 0: 
            return 0

        l,r= 0,0
        summ = 0
        res = 0

        l2 = 0
        summ2 = 0

        c = 0
        prev = None

        for num in nums:
            if num == prev:
                c += 1
            else:
                prev = num
                c = 1
            while nums[l] < num - k:
                summ -= 1
                l+= 1

            while r < n and nums[r] <= num + k:
                summ += 1
                r += 1
            res = max(res, c + min(summ - c, numOperations))

            summ2 += 1
            while nums[l2] < num - 2 * k:
                summ2 -= 1
                l2 += 1
            res = max(res, min(summ2, numOperations))

        return res 