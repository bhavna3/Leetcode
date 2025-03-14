class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        def canDistribute(mid):
            count = 0
            for c in candies:
                count += c // mid  # Count how many children can receive 'mid' candies
            return count >= k

        if sum(candies) < k:
            return 0  # Impossible to distribute at least one candy to each child

        left, right = 1, max(candies)  # Possible candy count range
        while left < right:
            mid = (left + right + 1) // 2
            if canDistribute(mid):
                left = mid  # Try higher candy count per child
            else:
                right = mid - 1  # Try lower candy count per child

        return left
        
        



            




            

        