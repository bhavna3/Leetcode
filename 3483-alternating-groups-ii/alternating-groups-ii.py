class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        w = 1
        ans = 0
        n = len(colors)
        for i in range(1, n+k-2 + 1):
            if colors[i % n] != colors[(i - 1 + n) % n]:
                w += 1
            else:
                w = 1
            if w >= k:
                ans += 1
        return ans
        