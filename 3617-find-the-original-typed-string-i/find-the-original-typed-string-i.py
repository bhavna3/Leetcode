class Solution:
    def possibleStringCount(self, word: str) -> int:
        sum=1
        for i in range(len(word)-1):
            if word[i]==word[i+1]:
                sum+=1
        return sum

        