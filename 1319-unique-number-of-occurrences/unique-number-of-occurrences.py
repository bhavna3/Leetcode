class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        freq={}
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1

        occurrences=set()
        for count in freq.values():
            if count in occurrences:
                return False
            else:
                occurrences.add(count)
        
        return True
                

                


        