class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_prof=0
        min_price=float('inf')

        for price in prices:
            if price<min_price:
                min_price=price

            profit=price-min_price

            if profit>max_prof:
                max_prof=profit

        return max_prof
