class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
 
        n = sorted(nums)
        vals = []

        for i,num in enumerate(n):

            if i > 0 and num == n[i - 1]:
                continue

            l = i + 1
            r = len(n)-1        

            while l < r:
                lval = n[l]
                rval = n[r]
                target = num * -1

                sum = lval + rval

                if sum == target:
                    if [num, lval, rval] not in vals:
                        vals.append([num, lval, rval])
                    l+1
                    r-=1
                elif sum < target:
                    l += 1
                else:
                    r -= 1
        return vals