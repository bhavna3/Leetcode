class Solution:
    def totalMoney(self, n: int) -> int:
        week=n//7 #full weeks = monday value
        rem_days=n%7

        total=28*week + 7*(week*(week-1))//2  # 28 per week fixed + additional 7 increase every week
        new_monday=week+1

        for i in range(1,rem_days+1): #O(6) 
            total+=new_monday+(i-1)             # full week (7days) + rem days (b/w 1-6)
        return total

        #better 
        #TC O(6 or 7)=O(1)
        #SC O(1)




