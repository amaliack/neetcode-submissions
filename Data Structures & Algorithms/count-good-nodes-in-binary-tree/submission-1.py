# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_val, count):
            if not root:
                return max_val, count
            if root.val >= max_val:
                count += 1

            max_val = max(max_val, root.val)
            left_max, left_count = dfs(root.left, max_val, 0)
            right_max, right_count = dfs(root.right, max_val, 0)            
            return max_val, left_count + right_count + count
        
        max_val, count = dfs(root, root.val, 0)
        return count
        
