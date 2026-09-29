class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        1. input constraints --> length of the arr is at least 2, numbers and targer -1000,1000
        2. empty input --> not possible, we are guaranteed a valid solution
        3. positive/negative --> both possible
        4. sorted --> yes, the input is sorted
        5. duplicates --> not relevant here
        6. modify input --> not necessary here
        7. edge case behaviors --> we are guaranteed a valid solution, and O(1) space

        brute force --> try every combination of indices and see what adds up O(n^2)
        invariant:
        - here the repeated work is checking each pair of indices
        - since the input is sorted, we can take advantage of that fact
        """

        left = 0
        right = len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
        return []
            

