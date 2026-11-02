class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force --> O(N^2) where we go through each element and the rest of array

        # could be some intuition with the stack, where we compare top of stack to curr
        stack = []
        res = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            if not stack:
                stack.append((index, temp))
                continue
            
            top_index, top_val = stack[-1]
            while stack and temp > top_val:
                res[top_index] = index - top_index
                stack.pop()
                if stack: top_index, top_val = stack[-1]
            stack.append((index, temp))
        return res
            
