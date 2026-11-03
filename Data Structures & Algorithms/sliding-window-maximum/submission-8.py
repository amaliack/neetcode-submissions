class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        window_map = defaultdict(int)

        # initialize the heap with first window
        for i in range(k):
            heapq.heappush(heap, -1 * nums[i])
            window_map[nums[i]] += 1
        res.append(-1 * heap[0])

        # now we evaluate each subsequent window
        for j in range(k, len(nums)):
            new_el = nums[j]
            leaving = nums[j - k]
            window_map[leaving] -= 1

            heapq.heappush(heap, -1 * new_el)
            window_map[new_el] += 1

            while heap and window_map[-heap[0]] == 0:
                heapq.heappop(heap)
        
            res.append(-1 * heap[0])
        return res

