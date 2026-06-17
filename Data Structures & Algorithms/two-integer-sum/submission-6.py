class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        enums = [(num, i) for i, num in enumerate(nums) ]
        sorted_nums = sorted(enums, key=lambda item:item[0])
        
        left = 0
        right = len(sorted_nums) - 1
    
        while left < right:
            left_val, left_index = sorted_nums[left]
            right_val, right_index = sorted_nums[right]

            s = left_val + right_val
            if s == target:
                break
            elif s < target:
                left += 1
            else:
                right -= 1
        
        return sorted([left_index, right_index]) 
