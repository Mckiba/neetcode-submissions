class Solution:
    def search(self, nums: List[int], target: int) -> int:


        l, r = 0, len(nums) - 1

        # nums=[5,[1],3] 3


        
        while l <= r:

            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:  #left is sorted
                if nums[l] <= target and nums[mid] >= target: #number is here
                    r = mid - 1
                else:  
                    l = mid + 1


            elif nums[r] >= nums[mid]: #right is sorted
                if nums[mid] <= target and nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
            else: 
                break
         
            
 
        return - 1
            

    
        
        #     mid = l + (r - l) // 2
        #     print("MID",mid)
        #     if nums[mid] == target:
        #         return mid

        #     print(mid, l, r)
        #     if nums[l] >= target <= nums[mid]:
        #         print("TRUE")
        #         l = mid + 1
        #         print(nums[l:r+1]) 
        #     elif target < nums[r] or target < nums[mid]:
        #         r = mid - 1
        #         print("ELSE")
        #         print(nums[l:r+1]) 
        # return -1  

        
        
        