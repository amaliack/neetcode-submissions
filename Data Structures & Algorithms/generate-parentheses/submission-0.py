class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(left, right, curr):
            # base case: we have n left and n right
            if left == n and right == n:
                res.append(curr)
                return
            
            # we can add ( if left count < n
            if left < n:
                curr += "("
                dfs(left + 1, right, curr)
                curr = curr[:-1]

            if right < left:
                curr += ")"
                dfs(left, right + 1, curr)
                curr = curr[:-1]

        dfs(0, 0, "")
        return res
