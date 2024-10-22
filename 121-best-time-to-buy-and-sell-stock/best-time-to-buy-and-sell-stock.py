class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price=float('inf')
        max_prof=0

        for price in prices:
            if price<min_price:
                min_price=price

            prof=price-min_price

            if prof>max_prof:
                max_prof=prof

        return max_prof

