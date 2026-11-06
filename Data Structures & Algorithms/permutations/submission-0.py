class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # there are n! permutations of a set of numbers
        # we can do a n choices --> (n - 1) choices --> ... --> 1 choice

        res = []
        def dfs(curr_nums):
            # base case: length of curr_nums == n
            if len(curr_nums) == len(nums):
                res.append(list(curr_nums.copy()))
                return
            
            for j in range(len(nums)):
                if nums[j] in curr_nums:
                    continue
                
                curr_nums.append(nums[j])
                dfs(curr_nums)
                curr_nums.pop()
        
        dfs([])
        return res
