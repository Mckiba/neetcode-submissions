class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        enums = [(num, i) for i, num in enumerate(nums) ]
        nums_sorted = sorted(enums, key=lambda x:x[0])

        l = 0
        r = len(nums_sorted) - 1

        while l < r:
            
            lval, li = nums_sorted[l]
            rval, ri = nums_sorted[r]

            s = lval + rval

            if s == target:
                break
            elif s < target:
                l += 1
            else: 
                r -= 1
        return  sorted([li,ri])

        