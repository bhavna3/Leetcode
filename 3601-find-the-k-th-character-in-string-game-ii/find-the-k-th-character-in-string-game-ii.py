class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n, i = 1, 0
        while n < k:
            n *= 2
            i += 1
        shift = 0
        while n > 1:
            if k > n // 2:
                k -= n // 2
                shift += operations[i - 1]
            n //= 2
            i -= 1
        return chr(shift % 26 + ord("a"))