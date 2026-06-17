class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights)-1
        cap = 0

        while l < r:
            lval = heights[l]
            rval = heights[r]

            sum = (r - l) * (min(lval, rval)) 
            if sum > cap:
                cap = sum 

            if lval <= rval:
                l += 1
            else:
                r -= 1
            

        return cap