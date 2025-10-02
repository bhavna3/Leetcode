class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty=numBottles
        while empty>=numExchange:
            numBottles+=1
            empty=empty-numExchange+1
            numExchange+=1
        return numBottles