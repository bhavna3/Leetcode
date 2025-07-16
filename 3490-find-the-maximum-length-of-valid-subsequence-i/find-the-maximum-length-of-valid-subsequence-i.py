class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n=len(nums)
        if n==2: 
            return 2
        z=nums[0]&1
        L=[1-z, z, 1]
        for num in nums[1:]:
            x=num&1
            L[x&1]+=1
            if x!=z:
                L[2]+=1
                z=1-z
        return max(L)