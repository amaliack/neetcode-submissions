class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr_nums, curr_sum):
            if curr_sum == target:
                res.append(curr_nums.copy())
                return
                
            if i >= len(candidates) or curr_sum > target:
                return
                 
            # decision: we add this element
            curr_nums.append(candidates[i])
            dfs(i + 1, curr_nums, curr_sum + candidates[i])

            # decision: we don't what this element
            curr_nums.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr_nums, curr_sum)

        dfs(0, [], 0)
        return res      
