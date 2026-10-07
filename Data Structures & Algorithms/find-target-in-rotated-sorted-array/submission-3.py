class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [4, 5, 0, 1, 2, 3, 4]
        # case 1: if left < mid = left side is sorted
        # case 2: if right > mid = right side is sorted
        # case 3: if left > mid or if right > mid
        #   --> we need to check with target
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            
            # left sorted portion
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1




        