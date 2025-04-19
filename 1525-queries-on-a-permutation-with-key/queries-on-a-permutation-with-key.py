class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        result = []
        
        mList = [x for x in range(1, m + 1)]
        
        for x in queries:
            result.append(mList.index(x))
 
            mList.remove(x)
 
            mList.insert(0, x)
        
        return result