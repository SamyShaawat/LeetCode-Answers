class Solution:     
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        num, den = abs(numerator), abs(denominator)
        result = [sign + str(num // den)]
        rem = num % den
        if rem == 0:
            return "".join(result)
        result.append(".")
        seen = {}
        while rem != 0:
            if rem in seen:
                pos = seen[rem]
                return "".join(result[:pos]) + "(" + "".join(result[pos:]) + ")"
            seen[rem] = len(result)
            rem *= 10
            result.append(str(rem // den))
            rem %= den

        return "".join(result)