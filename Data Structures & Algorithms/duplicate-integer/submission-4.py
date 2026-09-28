class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        1. input --> (1) nums.length < 10^5 and (2) nums[i] is within 10^9
        2. empty input --> yes (can be length 0m but numbers good)
        3. duplicates --> we are looking for them
        4. positive/negative --> all integers pos or neg
        5. sorted input --> not relevant, and no
        6. modify input --> not needed
        7. edge case --> none possible really

        brute force --> the straightforward approach is O(n^2)
        --> two for loops that we individually check each element against entire

        invariant --> bottleneck is repeated checking of elements = hash set
        """

        map = defaultdict(int)
        for n in nums:
            if map[n]:
                return True
            else:
                map[n] += 1
        return False
