class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st = []

        for n in nums:
            while st:
                g = gcd(st[-1], n)
                if g == 1:
                    break
                n = (st.pop() * n) // g
            st.append(n)

        return st