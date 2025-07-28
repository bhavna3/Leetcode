class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for n in nums:
            max_or |= n

        def dfs(i, curr):
            if i == len(nums):
                return 1 if curr == max_or else 0
            include = dfs(i + 1, curr | nums[i])
            exclude = dfs(i + 1, curr)
            return include + exclude

        return dfs(0, 0)