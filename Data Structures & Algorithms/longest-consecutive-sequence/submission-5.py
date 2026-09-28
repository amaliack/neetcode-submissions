class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        max_len = 0

        for num in nums:
            if map[num - 1] == 0:
                length = 0
                while map[num + length]:
                    length += 1
                max_len = max(max_len, length)
        return max_len