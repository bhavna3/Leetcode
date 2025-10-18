class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 1
        minn = nums[0]-k

        for num in nums[1:]:
            if(minn < num - k):
                minn = num - k
                count+=1
            elif(minn < num + k):
                minn = minn + 1
                count+=1

        return count