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

        nums.sort()
        list_of_sols = []
        for i in range(len(nums)):
            # pruning and getting rid of duplicates
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    list_of_sols.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # gets rid of duplicates
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    left += 1

        return list_of_sols






