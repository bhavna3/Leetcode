# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.output_list = []

        def helper(node, h) : 
            if not node : return 
            if len(self.output_list) == h : 
                self.output_list.append([])
            self.output_list[h].append(node.val)
            helper(node.left, h + 1)
            helper(node.right, h + 1)


        helper(root, 0)
        return self.output_list   