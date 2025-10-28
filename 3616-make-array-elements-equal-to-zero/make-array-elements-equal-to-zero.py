class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
       
        tot = sum(nums)
        l = 0 
        count = 0 
        
        for i in range(n):
            r= tot-l
            if nums[i] == 0:
                if r==l:
                    count += 2 
       
                elif abs(r-l) == 1:
                    count += 1 
        
            l += nums[i]
            
        return count