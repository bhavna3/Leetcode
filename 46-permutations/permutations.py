class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n=len(nums)
        res, sol=[], []

        def backtrack():
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()

            if len(sol)==n:
                res.append(sol[:])
                return

        backtrack()
        return res
        