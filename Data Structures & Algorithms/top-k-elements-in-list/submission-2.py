class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. we have a min-heap of size k
        # 2. we have a hash-map to get frequencies (or Counter)

        counts = Counter(nums)
        heap = []
        for item, freq in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, item))
            else:
                if freq > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq, item))
        return [item for freq, item in heap]