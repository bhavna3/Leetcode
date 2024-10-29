class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def bt(start, path):
            if len(path) == k:
                results.append(path.copy()) #append a current copy of path as lists are mutable
                return
            
            for i in range(start, n+1):
                path.append(i)
                bt(i+1, path)
                path.pop()
        
        results = []
        bt(1, [])
        return results