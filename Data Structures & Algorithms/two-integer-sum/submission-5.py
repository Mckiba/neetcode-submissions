class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #get a sorted list of keys and values
        enum_nums = [(num, i) for i, num in enumerate(nums)]
        sorted_nums = sorted(enum_nums, key=lambda item:item[0])

        #two pointer search 


        #two pointters 
        #if sum > target, need a smaller sum so decrease right, right -= 1 
        #if sum < target we need a bugger sum so imcrease left left +=1
        #if sum equals target we good 



        left = 0
        right = len(sorted_nums) - 1

        while left < right:

            left_val, left_index = sorted_nums[left]
            right_val, right_index = sorted_nums[right]

            s = left_val + right_val

            if s == target:
                return sorted([left_index, right_index])
            elif s < target:
                left += 1
            else:
                right -= 1
