class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = set(nums)
        max_len = 0

        for num in nums:
            if (num - 1) not in map:
                length = 0
                while (num + length) in map:
                    length += 1
                max_len = max(max_len, length)
        return max_len