# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # some recursive function where we compare p, q and "root"
        # since BST, if p <= root <= q, we know that they are in separate subtrees
        # therefore, we return whatever root satisfies this
        # if both < root or both > root we choose that tree

        def helper(root: TreeNode, p: TreeNode, q: TreeNode):
            if not root:
                return root
            
            if p.val <= root.val <= q.val:
                return root
            
            if p.val <= q.val <= root.val:
                return helper(root.left, p, q)
            else:
                return helper(root.right, p, q)
            
        smaller = p if p.val < q.val else q
        larger = p if p.val > q.val else q
        return helper(root, smaller, larger)




