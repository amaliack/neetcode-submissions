class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        
        max_len = 1
        for num in nums:
            if map[num + 1] and map[num - 1] == 0:
                count = 1
                temp_max = 1
                while map[num + count]:
                    temp_max += 1
                    count += 1
                max_len = max(max_len, temp_max)
        return max_len