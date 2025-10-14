class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if 2*k>len(nums):
            return False

        def inc(subarray):
            for i in range(len(subarray)-1):
                if subarray[i]>=subarray[i+1]:
                    return False
            return True

        
        n=len(nums)
        for i in range(n-2*k+1):
            first=nums[i:i+k]
            second=nums[i+k:i+2*k]


            if inc(first) and inc(second):
                return True

        return False


