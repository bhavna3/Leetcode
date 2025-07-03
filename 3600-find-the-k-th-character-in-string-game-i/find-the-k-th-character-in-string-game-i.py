class Solution:
    def kthCharacter(self, k: int) -> str:
        word='a'
        
        while len(word)<k:
            s=''
            for val in word:
                if val=='z':
                    s+=a
                else:
                    s+=chr(ord(val)+1)
            word+=s

        return word[k-1]

        