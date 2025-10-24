class Solution:
    def bal(self, n: int) -> bool:
        s={}
        while n>0:
            d=n%10
            s[d]=s.get(d,0)+1
            n //= 10

        
        for x, freq in s.items():
            if x != freq:
                return False
        return True

    def nextBeautifulNumber(self, n: int) -> int:
        i = n + 1
        while True:
            if self.bal(i):
                return i
            i += 1
