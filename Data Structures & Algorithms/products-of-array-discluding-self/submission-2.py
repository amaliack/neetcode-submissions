class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [1] * n
        suffix_prod = [1] * n

        forward_prod = 1
        backward_prod = 1
        for i in range(n - 1):
            forward_prod *= nums[i]
            prefix_prod[i + 1] = forward_prod

            backward_prod *= nums[n - 1 - i]
            suffix_prod[n - 2 - i] = backward_prod
        
        output = [prefix_prod[i] * suffix_prod[i] for i in range(n)]
        return output
        


    
            