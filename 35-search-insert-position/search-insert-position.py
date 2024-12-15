class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if target > nums[n-1]:
            return n
        if target < nums[0]:
            return 0
        first, last, mid = 0, n-1, -1
        while first <= last:
            mid = (last + first) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                first = mid + 1
            else:
                last = mid - 1
        if target < nums[mid]:
            return mid
        else:
            return mid + 1

        