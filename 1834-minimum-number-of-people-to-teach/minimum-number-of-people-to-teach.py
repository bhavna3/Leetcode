class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        s = set()
        for u, v in friendships:
            u -= 1
            v -= 1
            ok = False
            for x in languages[u]:
                if x in languages[v]:
                    ok = True
                    break
            if not ok:
                s.add(u)
                s.add(v)

        ans = len(languages) + 1
        for i in range(1, n + 1):
            can = 0
            for v in s:
                if i not in languages[v]:
                    can += 1
            ans = min(ans, can)
        return ans