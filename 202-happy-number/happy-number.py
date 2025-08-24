class Solution:
    def isHappy(self, n: int) -> bool:
        

        def returnSq(n: int) -> int:
            sqSum = 0
            while(n > 0):
                temp = n % 10
                sqSum += temp ** 2
                n = n // 10
            return sqSum

        res = set()
        while n not in res:
            res.add(n)
            n = returnSq(n)

            if(n == 1):
                return True
        return False
