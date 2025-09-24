class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        n=numerator
        d=denominator 

        if n==0:
            return '0'

        res=[]

        if (n<0) ^ (d<0):
            res.append('-')

        n, d = abs(n), abs(d)

        res.append(str(n // d))
        rem=n%d

        if rem == 0:
            return "".join(res)
        res.append(".")

        rem_map = {}
        while rem != 0:
            if rem in rem_map:
                res.insert(rem_map[rem], "(")
                res.append(")")
                break
            
            rem_map[rem] = len(res)
            
            rem *= 10
            res.append(str(rem // d))
            rem %= d

        return ''.join(res)