class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # data structure --> dictionary
        num_dict = {}
        for num in nums:
            if num in num_dict:
                return True
            else:
                num_dict[num] = 1
        return False