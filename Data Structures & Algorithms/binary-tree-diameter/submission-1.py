# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def maxDepth(root: Optional[TreeNode]):
            if not root:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        maxDepth(root)
        return self.res
