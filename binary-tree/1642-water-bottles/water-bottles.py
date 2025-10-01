class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        drink = numBottles
        while drink >= numExchange:
            ans += (drink // numExchange)
            drink = (drink % numExchange) + (drink // numExchange)

        return ans 

