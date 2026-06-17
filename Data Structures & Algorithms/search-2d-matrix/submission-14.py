class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = l + (r -l) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif target > matrix[mid][-1]:  
                l = mid + 1
            else:
                r = mid -1

        t_arr = matrix[mid]
        l, r = 0, len(t_arr) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if t_arr[mid] == target:
                return True
            elif t_arr[mid] > target:
                r = mid - 1
            else: 
                l = mid + 1
        return False