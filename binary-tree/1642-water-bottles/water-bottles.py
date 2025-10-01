class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numExchange >= 2:
            return (numBottles + (numBottles - 1) // (numExchange - 1))
        else:
            ans = numBottles
            drink = numBottles
            while drink >= numExchange:
                ans += (drink // numExchange)
                drink = (drink % numExchange) + (drink // numExchange)

            return ans 

