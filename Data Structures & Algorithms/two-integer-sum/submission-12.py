class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        memory = {} #value: index

        # check difference between num and target, does that diff exist in our hash map,
        # if yes then we return the index and the current index

        for index, num in enumerate(nums):
            diff = target - num
            if diff in memory:
                return sorted([memory[diff], index])
            else:
                memory[num] = index
        return []



        