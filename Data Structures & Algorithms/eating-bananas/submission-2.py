class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we want to find minimum k-value
        # search space: [0, sum(piles)]
        # we need to define a checker that determines if this k is feasible to eat all

        total_bananas = sum(piles)
        def isFeasible(k: int) -> bool:
            curr_el = 0
            hours_taken = 0
            while curr_el < len(piles):
                bph = min(k, piles[curr_el])
                hours_taken += math.ceil(piles[curr_el] / bph)
                curr_el += 1
            return True if hours_taken <= h else False
                
        
        l = 1
        r = total_bananas
        while l < r:
            mid = l + (r - l) // 2
            if isFeasible(mid):
                r = mid
            else:
                l = mid + 1
        return l