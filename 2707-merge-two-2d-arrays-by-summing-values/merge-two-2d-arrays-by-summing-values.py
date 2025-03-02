class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        i = 0
        j = 0
        l1 = len(nums1)
        l2 = len(nums2)
        while i < l1 and j < l2:
            if nums1[i][0] == nums2[j][0]:
                res.append(nums1[i])
                res[-1][1] = nums1[i][1] + nums2[j][1]
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        while i < l1:
            res.append(nums1[i])
            i += 1

        while j < l2:
            res.append(nums2[j])
            j += 1
            
        return res


        