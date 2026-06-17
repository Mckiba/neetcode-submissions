class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        enum_nums = list(enumerate(nums))

        sorted_nums = sorted(enum_nums, key=lambda item: item[1])
        print(sorted_nums)
        
        for i in range(len(sorted_nums)):
            for j in range(i+1, len(sorted_nums)):
                if sorted_nums[i][1] + sorted_nums[j][1] == target:
                    if sorted_nums[i][0] > sorted_nums[j][0]:
                        return [sorted_nums[j][0], sorted_nums[i][0]]
                    else: 
                        return [sorted_nums[i][0], sorted_nums[j][0]]
            
            

        return nums

        #nums=[3,2,3]
        #i = 0
        #j = 1
        #2 + 3 = 6 X

        #i = 1
        #j = 2
       
       #if 3 > 2
       #[2, 0]
       #
        
        



    
        