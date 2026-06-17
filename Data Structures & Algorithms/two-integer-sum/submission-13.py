class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        memory = {} #value: index

        for index, num in enumerate(nums):
            diff = target - num
            if diff in memory:
                return sorted([memory[diff], index])
            memory[num] = index
        return []        