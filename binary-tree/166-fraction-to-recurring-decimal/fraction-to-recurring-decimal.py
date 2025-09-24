class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        ans = []

        if (numerator < 0) ^ (denominator < 0):
            ans.append("-")

        numerator, denominator = abs(numerator), abs(denominator)

        ans.append(str(numerator // denominator))
        remainder = numerator % denominator

        if remainder == 0:
            return "".join(ans)

        ans.append(".")

        remainder_pos = {}

        while remainder != 0:
            if remainder in remainder_pos:
                idx = remainder_pos[remainder]
                ans.insert(idx, "(")
                ans.append(")")
                break

            remainder_pos[remainder] = len(ans)

            remainder *= 10
            ans.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(ans)
