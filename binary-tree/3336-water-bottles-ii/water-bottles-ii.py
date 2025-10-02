class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drink = numBottles
        while numExchange <= numBottles:
            drink += 1
            numBottles -= numExchange
            numExchange += 1
            numBottles += 1

        return drink
        

        