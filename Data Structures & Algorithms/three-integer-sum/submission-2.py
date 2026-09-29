class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        1. input constraints --> nums length is at least 3
        2. empty input --> not possible
        3. positive/negative --> both are allowed
        4. duplicates --> only distinct indices are allowed
        5. sorted --> the input is not inherently sorted (but we might)
        6. modify input --> seems we can since indices aren't necessary
        7. edge case behavior --> possible that no triplets add up, order doesn't matter

        brute force --> check every single combination of 3 possible - O(n^3)
        invariant:
        - the repeated work in the brute force is having to check each triple
        - we could maybe modify 2Sum a bit, sort the list, and then use a hashmap for the diff
        - we have an outer for loop and and then run 2Sum on the inner for loop for other two
        """

        arr = sorted(nums)
        list_of_sols = []
        for i in range(len(nums)):
            if arr[i] > 0:
                break
            left = i + 1
            right = len(nums) - 1
            target = -1 * arr[i]
            while left < right:
                curr_sum = arr[left] + arr[right]
                if curr_sum == target:
                    list_of_sols.append([arr[i], arr[left], arr[right]])
                    left += 1
                    right -= 1
                elif curr_sum > target:
                    right -= 1
                else:
                    left += 1
        return list(set(tuple(item) for item in list_of_sols))






