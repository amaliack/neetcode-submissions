class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # (index, height)
        stack = []
        max_area = float('-inf')
        for right, height in enumerate(heights):
            if not stack:
                stack.append((right, height))
                continue
            
            left, top_height = stack[-1]
            add_index = right
            while stack and top_height > height:
                max_area = max(max_area, (right - left) * top_height)
                stack.pop()
                add_index = left
                if stack: left, top_height = stack[-1]
            stack.append((add_index, height))
        
        # we need to process whatever's remaining in the stack
        print(stack)
        n = len(heights)
        while stack:
            left, height = stack.pop()
            max_area = max(max_area, (n - left) * height)

        return max_area

