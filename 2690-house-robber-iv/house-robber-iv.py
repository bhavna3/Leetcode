class Solution(object):
    def minCapability(self, nums, k):
        def can_rob(res, houses, k):
            count = 0
            i = 0
            while i < len(houses):
                if houses[i] <= res:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count >= k:
                    return True
            return False

        low, high = min(nums), max(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if can_rob(mid, nums, k):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        