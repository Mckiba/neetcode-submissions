class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      
        l, r = 0, len(matrix) - 1
        mid = int
        while l <= r:
            mid = l + (r -l) // 2 # 1

            

            if min(matrix[mid]) <= target <= max(matrix[mid]): # if 10 <= 15 <=13 
                break
            elif target > max(matrix[mid]): # 15 > 13
                l = mid + 1 # l = 
            else:
                r = mid -1
        
        # check if num is in mid
        print("MID",mid)
        print("FINAL MATRXI",matrix[mid])
        if target in matrix[mid]:
            return True

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

        # r = mid - 1

        # if matrix[mid[0]] < target:
        #     l = mid 
        # else 
        # r = mid - 1 


        #find the matrix containing the value 
        # find index of the value in matrix




