class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
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
        return - 1