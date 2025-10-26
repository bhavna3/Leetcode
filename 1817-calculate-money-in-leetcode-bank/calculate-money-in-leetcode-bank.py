class Solution:
    def totalMoney(self, n: int) -> int:
        week=n//7 #full weeks = monday value
        rem_days=n%7

        return 28*week + 7*(week*(week-1))//2  + rem_days*(2*(week+1)+(rem_days-1))//2 
        #arithmetic progression formula

        #Optimal 
        #TC O(1) 
        #SC O(1)





