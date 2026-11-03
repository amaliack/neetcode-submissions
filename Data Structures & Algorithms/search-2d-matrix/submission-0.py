class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find which row
        l = 0
        r = len(matrix) - 1
        row_num = None
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row_num = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1    
        if row_num is None: return False

        # find within that row
        l = 0
        r = len(matrix[row_num]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target > matrix[row_num][mid]:
                l = mid + 1
            elif target < matrix[row_num][mid]:
                r = mid - 1
            else:
                return True
        return False
