class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n=len(nums)
        ans=nums[0]
        l=1
        for k in range(1, n):
            l=l*(n-k)//k
            ans=(ans+nums[k]*l)%10
        return ans

        