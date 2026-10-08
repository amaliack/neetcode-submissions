# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root_curr, subroot_curr):
            if (not root_curr and subroot_curr) or (not subroot_curr and root_curr):
                return False
            
            if root_curr and subroot_curr and root_curr.val == subroot_curr.val:
                return dfs(root_curr.left, subroot_curr.left) and dfs(root_curr.right, subroot_curr.right)
            elif root_curr and subroot_curr and root_curr.val != subroot_curr.val:
                return False
            else:
                return True
                
        stack = [root]
        while stack:
            curr = stack.pop()
            if dfs(curr, subRoot):
                return True
            if curr:
                stack.append(curr.left)
                stack.append(curr.right)
        return False







