MOD = 10**9 + 7

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:

        @lru_cache(None)
        def dp(remaining, req, curr, carry):
            
            if remaining < 0 or req < 0 or remaining + carry.bit_count() < req:
                return 0
            if remaining == 0:
                if req== carry.bit_count():
                    return 1
                else:
                    return 0
            if curr >= len(nums):
                return 0
                
            res= 0
            for count in range(remaining + 1):

                combinatorial = math.comb(remaining, count) * pow(nums[curr], count, MOD) % MOD

                new = carry + count
                new_carry = new// 2
                new_lsb = new % 2
                
                res += combinatorial * dp(remaining - count, req - new_lsb, curr + 1, new_carry)
            return res % MOD
        return dp(m, k, 0, 0)
        