class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix=[[1,2,4,8],[10,11,12,13],[14,20,30,40]]
        # target=10

        l, r = 0, len(matrix) - 1
        mid = int
        while l <= r:
            mid = l + (r -l) // 2
            arr = matrix[mid]
            if arr[0] <= target <= arr[len(arr)-1]:
                break
            elif target > arr[len(arr)-1]:  
                l = mid + 1
            else:
                r = mid -1

        t_arr = matrix[mid]
        print(t_arr)
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
        

        
        


        # array now is the start of all the other array 
     


    


        # mid = len(matrix) // 2 
    
        # if targer in range(mid[0], mid[len])
            # return true

        # else if target > range(mid)
        # l - mid + 1

        # else 
        # r = mid - 1

       

    


