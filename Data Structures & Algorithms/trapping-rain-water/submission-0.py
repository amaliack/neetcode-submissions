class Solution:
    def trap(self, height: List[int]) -> int:
        left_temp_max = 0
        right_temp_max = 0
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        for i in range(len(height)):
            left_temp_max = max(height[i], left_temp_max)
            left_max[i] = left_temp_max

            right_index = len(height) - i - 1
            right_temp_max = max(height[right_index], right_temp_max)
            right_max[right_index] = right_temp_max
         
        trapped_water = 0
        curr = 1
        while curr < len(height) - 1:
            trapped_water += max(min(left_max[curr], right_max[curr]) - height[curr], 0)
            curr += 1
        return trapped_water





