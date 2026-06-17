class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      
        l, r = 0, len(matrix) - 1
        mid = int
        while l <= r:
            mid = l + (r -l) // 2
            arr = matrix[mid]
            if arr[0] <= target <= arr[len(arr)-1] and target in arr: 
                return True
            elif target > arr[len(arr)-1]:  
                l = mid + 1
            else:
                r = mid -1
        return False

        


        # array now is the start of all the other array 
     


    


        # mid = len(matrix) // 2 
    
        # if targer in range(mid[0], mid[len])
            # return true

        # else if target > range(mid)
        # l - mid + 1

        # else 
        # r = mid - 1

       

    


