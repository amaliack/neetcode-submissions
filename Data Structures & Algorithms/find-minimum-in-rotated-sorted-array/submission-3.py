class Solution:
    def findMin(self, nums: List[int]) -> int:
        # in this case, I think we just need to find the pivot
        # pivot: if the element to the right is lesser (that's the min!)
        # wrap-around formula
        #   --> right sided: (index + 1) % len(nums)
        #   --> left sided: (index - 1 + len(nums)) % len(nums)

        l = 0
        r = len(nums) - 1
        min_el = float('inf')
        while l < r:
            mid = l + (r - l) // 2
            min_el = min(nums[mid], min_el, nums[l], nums[r])
            # left sorted portion
            if nums[mid] < nums[r]:
                r = mid
            # right sorted portion
            else:
                l = mid + 1
        return nums[l]

