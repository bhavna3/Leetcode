class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        l = len(s)

        def explore(index, curr):
            if index >= l:
                result.append(curr.copy())

            for i in range(index, l):
                ss= s[index:i + 1]
                if ss == ss[::-1]:
                    curr.append(ss)
                    explore(i + 1, curr)
                    curr.pop()

        explore(0, [])
        return result