# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.retList = []

        def DFS(node):
            if node:
                self.retList.append(node.val)
                DFS(node.right)
                DFS(node.left)
            return
        
        DFS(root)
        return reversed(self.retList)