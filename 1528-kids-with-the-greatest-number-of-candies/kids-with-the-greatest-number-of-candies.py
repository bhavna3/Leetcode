class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        great = max(candies)  
        result = [(candy + extraCandies) >= great for candy in candies] 
        return result
            
        