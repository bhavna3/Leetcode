class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        count = numBottles  
        empty = numBottles

        while empty >= numExchange:
            new = empty // numExchange  
            count += new
            empty = empty % numExchange + new

        return count


        