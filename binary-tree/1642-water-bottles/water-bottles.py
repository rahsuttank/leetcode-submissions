class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty = 0
        drink = numBottles
        while drink >= numExchange:
            ans += (drink // numExchange)
            drink = (drink % numExchange) + (drink // numExchange)
            # print(drink)
            

        return ans 

