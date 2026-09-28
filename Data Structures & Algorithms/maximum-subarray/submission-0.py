class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        1. input --> length < 100,000 and numbers are between -10,000 and 10,000
        2. empty input --> no, the list must be at least 1
        3. duplicates --> definitely possible, but existence doesn't change
        4. positive/negative --> both
        5. sorted input --> no, and sorting would make this invalid
        6. modify input --> no, wouldn't help
        7. edge case --> could be possible the max sum is a negative and
           we can't just include/exclude based on pos/negative
        
        brute force --> get every combination of subarray possible and their sums
            --> this would be O(n^2)
        
        invariant --> this forces us to go over larger windows and recalculate even
        though we've already calculated the smaller components, so we can use a
        storage mechanism to prevent this from happening
            --> could be a dynamic programming solution
        """

        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum





