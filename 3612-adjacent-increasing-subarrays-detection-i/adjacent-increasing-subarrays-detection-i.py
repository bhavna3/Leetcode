class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prev=0
        s=0
        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] <= nums[i - 1]:
                length = i - s
                if prev >= k and length >= k or length >= 2 * k:
                    return True
                prev= length
                s = i
        return False