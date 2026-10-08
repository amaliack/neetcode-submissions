# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            temp_list = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    queue.append(curr.left)
                    queue.append(curr.right)
                    temp_list.append(curr.val)
            if temp_list: res.append(temp_list)
        return res
