class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}

        def helper(pre_start, in_start, in_end):
            if pre_start >= len(preorder) or in_start > in_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            index = inorder_map[root_val]
            left_size = index - in_start

            # Build left and right subtrees
            root.left = helper(pre_start + 1, in_start, index - 1)
            root.right = helper(pre_start + left_size + 1, index + 1, in_end)

            return root

        return helper(0, 0, len(inorder) - 1)