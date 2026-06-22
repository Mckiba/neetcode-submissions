class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        #[1,2,4,6] = 6 * 1 * 3 * 4
        #__________________
        #(0,1) [2,4,6] [1] = 48
        #(1,2) [1]     [4,6] = 24
        #(2,4) [1,2]   [6] = 12
        #(3,6) [1,2,4] [1] = 8
        res = []

      
        for i in range(len(nums)):
            l = math.prod(nums[:i])
            r = math.prod(nums[i+1:])
            res.append(l * r)

        return res
