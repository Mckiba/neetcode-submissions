class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      
        l, r = 0, len(matrix) - 1
        mid = int
        while l <= r:
            mid = l + (r -l) // 2
            arr = matrix[mid]
            if min(arr) <= target <= max(arr) and target in arr: 
                return True
            elif target > max(arr):  
                l = mid + 1 # l = 
            else:
                r = mid -1
        


        return False

        


        # array now is the start of all the other array 
     


        # mid = len(matrix) // 2 
        # mid = 1

        # if matrix[mid[0]] < target:
        #     l = mid 
        # else 
        # r = mid - 1 


        #find the matrix containing the value 
        # find index of the value in matrix




        # mid = len(matrix) // 2 
    
        # if targer in range(mid[0], mid[len])
            # return true

        # else if target > range(mid)
        # l - mid + 1

        # else 
        # r = mid - 1

       

    


