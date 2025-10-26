class Solution:
    def totalMoney(self, n: int) -> int:
        summ=0
        m=1
        day=1
        
        for i in range(1,n+1):
            summ+=m+(i-1)%7
            day+=1
            if day==8:
                m+=1
                day=1

        return summ   

        
        #bruteforce
        #TC O(n)
        #SC O(1)

