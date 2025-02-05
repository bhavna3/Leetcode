class Solution(object):
    def search(self, nums, target):

        N=len(nums)
        R=N-1
        L=0

        while L<=R:
            M=(L+R)//2

            if nums[M] == target:
                return M
            elif target<nums[M]:
                R=M-1
            else:
                L=M+1

        return -1

        